from pathlib import Path

from services.docx_template_processor import DocxTemplateProcessor
from services.parsing_config import ParsingConfig
from services.parsing_manager import ParserManager
from services.documents_settings import settings
from datetime import datetime


def process_document(pdf_input_path: str | Path, template_path: str | Path = "output/template.docx"):

    pc = ParsingConfig.from_json(settings)
    pm = ParserManager(pc, pdf_input_path)

    extracted_data = pm.parse()

    today = datetime.now().date()
    name = extracted_data.get("legal_business_name", "output").replace(" ", "_")
    output_path = f"output/{name}_{today}.docx"

    processor = DocxTemplateProcessor(template_path, output_path, extracted_data)
    processor.process_document()
    processor.save()