from langdetect import detect, detect_langs
import fitz
from pathlib import Path
import subprocess
from utils.logger import botlog
from services.parsing_config import ParsingConfig
from services.pdf_parsers.registry_certificate_parser import RegistryCertificateParser
from services.pdf_parsers.registro_mercantil_parser import RegistroMercantilParser


class ParserManager:
    def __init__(self, parsing_config: ParsingConfig, file_path: str | Path):
        self.parsing_config = parsing_config
        self.file_path = file_path
        self.language = None
        self.document_type = None
        self.text = None
        self.meta_title = None
        self.doc_type = None
        self.document_config = None
        self._analyze()

    def _analyze(self):
        """
        Determines the document type, its language, and config
        """
        botlog("Analyzing PDF...")
        self.text, self.language = self._extract_text_and_language_from_pdf(self.file_path)
        botlog(f"Detected language - {self.language}")
        self.meta_title = self._get_meta_title(self.file_path)
        botlog("Detecting document type...")
        self.doc_type = self._detect_document_type(self.text, self.language, self.meta_title)
        if not self.doc_type:
            botlog("Unable to determine document type", "ERROR")
            raise ValueError("Unable to determine document type")

        self.document_config = self.parsing_config.get_doc_config(self.doc_type, self.language)

    def parse(self):
        """
        Calls the corresponding parser.
        The parser must first be described as a separate class inherited from BaseParser
        """

        if self.doc_type == "registry_certificate":
            parser = RegistryCertificateParser(self.text, self.document_config, self.doc_type, self.language)
        elif self.doc_type == "registro_mercantil":
            parser = RegistroMercantilParser(self.text, self.document_config, self.doc_type, self.language)
        else:
            raise RuntimeError(f"Parser is not defined for {self.doc_type}")
        botlog("Parsing document...")
        return parser.parse(self.text)

    def _detect_document_type(self, text: str, language: str, meta_title: str = ""):
        """Determines the document type based on key markers."""
        lines = text.splitlines()
        scores = {}

        for document_type in self.parsing_config.get_document_types():
            doc_config = self.parsing_config.get_doc_config(document_type, language)
            if doc_config is None:
                continue
            markers = doc_config.get_doc_markers()

            if markers.get("meta_title") and markers["meta_title"].lower() in meta_title.lower():
                scores[document_type] = scores.get(document_type, 0) + 10

            if markers.get("title") and any(markers["title"].lower() in line.lower() for line in lines[:5]):
                scores[document_type] = scores.get(document_type, 0) + 10

            for keyword in markers.get("keywords", []):
                if keyword in text:
                    scores[document_type] = scores.get(document_type, 0) + 1

        return max(scores, key=scores.get, default=None)

    def _extract_text_and_language_from_pdf(self, input_pdf: str | Path) -> tuple[str, str]:
        """Extracts text from a PDF file. If no text layer is present, performs OCR. Returns text and language."""
        # map langdetect language codes to tesseract language codes
        lang_map = {
            "en": "eng",
            "ru": "rus",
            "uk": "ukr",
            "hr": "hrv",
            "de": "deu",
            "fr": "fra",
            "es": "spa",
            "it": "ita",
            "bg": "bul",
            "sr": "srp",
            "pl": "pol",
            "cs": "ces",
            "pt": "por",
        }

        text = self._get_text_layer(input_pdf)
        if text:
            language = detect(text)
        else:
            language = self._detect_pdf_language(input_pdf)
            ocr_lang = lang_map.get(language)
            if not ocr_lang:
                raise ValueError(f"OCR language is not defined for {language}")
            ocr_lang = f"{ocr_lang}+eng" if ocr_lang != "eng" else ocr_lang
            text = self._get_ocr_text(input_pdf, ocr_lang)

        return text, language

    def _get_text_layer(self, input_pdf: str | Path, page: int = None) -> str:
        """Extracts the text layer from a PDF."""
        with fitz.open(input_pdf) as doc:
            if page is not None:
                return doc[page].get_text().strip()
            return "".join(page.get_text().strip() for page in doc)

    def _get_meta_title(self, input_pdf: str | Path) -> str:
        """Extracts the meta-title tag from the PDF file."""
        with fitz.open(input_pdf) as pdf:
            return pdf.metadata.get("title", "")

    def _detect_pdf_language(self, input_pdf: str | Path) -> str:
        """Determines the language of the PDF based on the first page (OCR if necessary)."""

        test_alphabet = {"Latin": "eng", "Cyrillic": "rus"}
        possible_langs = []
        # for compatibility with pdf documents with text layer
        text_layer = self._get_text_layer(input_pdf, page=0)
        if text_layer:
            return detect(text_layer)

        tmp_dir = Path().resolve() / "tmp"
        tmp_dir.mkdir(parents=True, exist_ok=True)
        first_page_pdf = tmp_dir / "first_page.pdf"
        test_pdf = input_pdf

        with fitz.open(input_pdf) as doc:
            if len(doc) > 1:
                single_page_pdf = fitz.open()
                single_page_pdf.insert_pdf(doc, from_page=0, to_page=0)
                single_page_pdf.save(first_page_pdf)
                single_page_pdf.close()
                test_pdf = first_page_pdf

        for alphabet, lang in test_alphabet.items():
            text = self._get_ocr_text(test_pdf, lang)
            possible_langs.extend(detect_langs(text))

        if first_page_pdf.exists():
            first_page_pdf.unlink()

        return max(possible_langs, key=lambda x: x.prob).lang if possible_langs else None

    def _get_ocr_text(self, input_pdf: str | Path, lang: str) -> str:
        """Runs OCRmyPDF and returns the recognized text."""
        botlog("Running OCR...")
        tmp_dir = Path().resolve() / "tmp"
        tmp_dir.mkdir(parents=True, exist_ok=True)
        output_txt = tmp_dir / f'output_{lang}.txt'
        output_pdf = tmp_dir / f'output_{lang}.pdf'
        ocr_command = ['ocrmypdf', '--skip-text', '--sidecar', output_txt, '-l', lang, input_pdf, output_pdf]

        subprocess.run(ocr_command, check=True, timeout=60)

        with open(output_txt, 'r', encoding='utf-8') as f:
            text = f.read()

        output_txt.unlink()
        output_pdf.unlink()
        return text
