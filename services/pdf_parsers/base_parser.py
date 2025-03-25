import re
from abc import ABC, abstractmethod
from utils.extractor import Extractor
from services.document_config import DocumentConfig
import dateparser

from utils.logger import botlog


class BaseParser(ABC):

    def __init__(self, text: str, document_config: DocumentConfig, doc_type: str, language: str):
        self.config = document_config
        self.doc_type = doc_type
        self.language = language
        self.extractor = Extractor()
        self.text = self.apply_document_preprocessing(text)

    def apply_document_preprocessing(self, text):
        """Applies preprocessing to the entire document if specified in the config."""
        preprocessing_func = self.config.get_doc_preprocessing()

        if preprocessing_func:
            if isinstance(preprocessing_func, list):
                for func_name in preprocessing_func:
                    if hasattr(self, func_name):
                        processing_method = getattr(self, func_name)
                        value = processing_method(text)
            else:
                if hasattr(self, preprocessing_func):
                    processing_method = getattr(self, preprocessing_func)
                    text = processing_method(text)

        return text

    def apply_preprocessing(self, field_name, value):
        """Applies preprocessing to a specific field."""
        preprocessing_func = self.config.get_field_params(field_name).get("preprocessing")

        if preprocessing_func:
            if isinstance(preprocessing_func, list):
                for func_name in preprocessing_func:
                    if hasattr(self, func_name):
                        processing_method = getattr(self, func_name)
                        if isinstance(value, list):
                            value = [processing_method(item) for item in value]
                        else:
                            value = processing_method(value)
            else:
                if hasattr(self, preprocessing_func):
                    processing_method = getattr(self, preprocessing_func)
                    if isinstance(value, list):
                        return [processing_method(item) for item in value]
                    return processing_method(value)

        return value

    def apply_postprocessing(self, field_name, value):
        """Applies postprocessing to a specific field."""
        postprocessing_func = self.config.get_field_params(field_name).get("postprocessing")

        if postprocessing_func:
            if isinstance(postprocessing_func, list):
                for func_name in postprocessing_func:
                    if hasattr(self, func_name):
                        processing_method = getattr(self, func_name)
                        if isinstance(value, list):
                            value = [processing_method(item) for item in value]
                        else:
                            value = processing_method(value)
            else:
                if hasattr(self, postprocessing_func):
                    processing_method = getattr(self, postprocessing_func)
                    if isinstance(value, list):
                        return [processing_method(item) for item in value]
                    return processing_method(value)

        return value

    @abstractmethod
    def parse(self, text):
        pass

    def clean_string(self, value: str) -> str:
        """Cleans the string of unnecessary spaces and characters."""
        if not value:
            return value
        value = re.sub(r'\n+', ', ', value)
        return re.sub(r'\s+', ' ', value).strip()

    def normalize_email(self, value: str) -> str | None:
        """
        Extracts an email address from a string.
        """
        if not value:
            return value
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

        match = re.search(email_pattern, value)
        return match.group(0) if match else None

    def normalize_url(self, value: str) -> str | None:
        """
        Extracts the first valid URL from a string.
        Supports URLs with or without a protocol (http, https).
        """
        if not value:
            return value
        url_pattern = r'(https?:\/\/)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/\S*)?'

        match = re.search(url_pattern, value)
        return match.group(0) if match else None

    def format_date_iso(self, value: str) -> str:
        """
        Formats data to ISO format
        """
        try:
            value = dateparser.parse(value, languages=[self.language]).strftime("%Y-%m-%d")
        except Exception as e:
            botlog(f"Error format data {e}")
        return value
