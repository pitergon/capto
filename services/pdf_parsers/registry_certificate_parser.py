import re
from services.pdf_parsers.base_parser import BaseParser
from utils.extractor import Extractor
from utils.logger import botlog

class RegistryCertificateParser(BaseParser):

    def parse(self, text):

        extracted_data = {}

        fields = self.config.get_fields()

        for field_name, field_info in fields.items():
            start_keywords = field_info.get("start_keywords", [])
            end_keywords = field_info.get("end_keywords", [])
            start_symbols = field_info.get("start_symbols", [])
            end_symbols = field_info.get("end_symbols", [])
            regex = field_info.get("regex")

            prepared_text = self.apply_preprocessing(field_name, text)
            extracted_value = None

            if start_keywords and end_keywords:
                extracted_value = self.extractor.extract_between_keywords(prepared_text, start_keywords, end_keywords)
            elif start_symbols and end_symbols:
                extracted_value = self.extractor.extract_between_symbols(prepared_text, start_symbols[0],
                                                                         end_symbols[0])
            elif regex:
                extracted_value = self.extractor.extract_using_re(prepared_text, regex)

            extracted_value = self.apply_postprocessing(field_name, extracted_value)

            if extracted_value:
                if isinstance(extracted_value, list) and len(extracted_value) == 1:
                    extracted_data[field_name] = extracted_value[0]
                else:
                    extracted_data[field_name] = extracted_value

        botlog(f"Extracted {len(extracted_data)} fields from {len(fields)} defined fields")

        return extracted_data

    def clean_address(self, text: str) -> str:
        """
        Cuts an address and cleans from spaces and line breaks.
        You can add into patterns list different pattern for different languages
        """
        if not text:
            return text
        patterns = [
            r"Адрес\s+на\s+електронна\s+поща",
            r"Интернет\s+страница:"
            r"email"
            r"site:"
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.DOTALL)
            if match:
                text = text[:match.start()]

        text = self.clean_string(text)
        return text

    def split_directors_names(self, directors: str) -> list:
        """Splits directors into individual names."""
        directors_list = []
        for director in directors.split("\n"):
            if director:
                dir_name = director.split(", ")[0]
                dir_name = self.clean_string(dir_name)
                directors_list.append(dir_name)
        return directors_list

    @staticmethod
    def remove_number_from_end(value: str) -> str:
        """Removes a number from the end of a string."""
        if not value:
            return value
        return re.sub(r'([,\n]\s*)\d{14}$', '', value) if value else value
