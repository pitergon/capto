class DocumentConfig:
    def __init__(self, config_data, document_type, language):
        self.config_data = config_data
        self.document_type = document_type
        self.language = language

    def get_all_fields_names(self):
        """Returns a list of all fields for the current document"""
        return list(self.config_data.get('fields', {}).keys())

    def get_fields_names(self):
        """Returns a list of names of only enabled fields"""
        return [k for k, v in self.config_data.get('fields', {}).items() if v.get('enabled')]

    def get_fields(self):
        """Returns enabled fields for the current document"""
        return {k: v for k, v in self.config_data.get('fields', {}).items() if v.get('enabled')}

    def get_field_params(self, field_name):
        """Returns the parameters of a specific field"""
        return self.config_data.get('fields', {}).get(field_name, {})

    def get_doc_preprocessing(self):
        """Returns the preprocessing function for the entire document"""
        return self.config_data.get('document_preprocessing')

    def get_doc_markers(self):
        """Returns markers for the entire document"""
        return self.config_data.get('markers')

    def __str__(self):
        return str(self.config_data)

    def __repr__(self):
        return str(self.config_data)