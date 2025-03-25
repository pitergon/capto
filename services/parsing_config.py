from services.document_config import DocumentConfig


class ParsingConfig:
    def __init__(self, config_data):
        self.config_data = config_data

    @classmethod
    def from_json(cls, json_data):
        return cls(json_data)

    def get_document_types(self):
        """Returns all document types."""
        return list(self.config_data.keys())

    def get_languages(self, document_type):
        """Returns a list of languages for a specific document type."""
        return list(self.config_data.get(document_type, {}).get('languages', {}).keys())

    def get_doc_config(self, document_type: str, language: str):
        """Returns the config for a specific document type and language."""
        languages_configs = self.config_data.get(document_type, {}).get('languages', {})
        if language not in languages_configs:
            return None
        return DocumentConfig(languages_configs[language], document_type, language)

    def __str__(self):
        return str(self.config_data)

    def __repr__(self):
        return str(self.config_data)