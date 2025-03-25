import re
from services.pdf_parsers.base_parser import BaseParser
from utils.extractor import Extractor
from utils.logger import botlog

class RegistroMercantilParser(BaseParser):

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


