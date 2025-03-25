# Document Processing System

## Requirements

To run this system, you need the following dependencies:
- **Tesseract OCR** must be installed on your system.
- Install required dependencies using:
  ```bash
  pip install -r requirements.txt
  ```

## How It Works

The system processes documents based on a **configuration file** that specifies document types, languages, and fields to extract from PDFs.

### Processing Steps
1. **Document Identification**: The system determines the most likely document type based on predefined markers.
2. **Field Extraction**: Extracts fields according to their configuration.
3. **Text Processing**: Supports pre-processing and post-processing for better extraction.
4. **Template Filling**: Uses placeholders in a DOCX template to insert extracted data.

### Extraction Methods
The system extracts data using:
- **Start and end keywords**
- **Start and end symbols**
- **Regular expressions**
- **Preprocessing and postprocessing commands**

The system operates using the text layer of the PDF. If there is no text layer, it can recognize the text using OCR. The language used for OCR is determined based on the first page's text.

## Configuration File Structure

The configuration file contains:

### Document Markers
Used to identify the document type based on:
- **Meta title**
- **Title in the first 5 lines**
- **Keywords in the first 10 lines**

### Field Parameters
Each field has specific parameters, such as:

- **`enabled`** (`true/false`): Enables or disables field extraction.
- **`extraction_level`** (`"required"`, `"optional"`, etc.): Defines the importance level of extraction for reporting.
- **`start_keywords`** (`[]`): List of keywords that indicate the start of the field.
- **`start_symbols`** (`[]`): List of symbols that indicate the start of the field.
- **`end_keywords`** (`[]`): List of keywords that indicate the end of the field.
- **`end_symbols`** (`[]`): List of symbols that indicate the end of the field.
- **`regex`** (`""`): Regular expression pattern for extracting the field.
- **`preprocessing`** (`[]`): List of preprocessing methods from parser class applied to the entire text before extracting the field.
- **`postprocessing`** (`[]`): List of postprocessing methods from parser class applied to the extracted field value.

Example:
```json
"languages": {
    "en": {
        "markers": {
            "meta_title": "EPZEUS",
            "title": "EPZEUS",
            "keywords": [
                "EPZEUS",
                "Commercial register and register of non-profit legal"
            ]
        },
        "document_preprocessing": "prepare_text",
        "fields": {
            "legal_business_name": {
                "enabled": true,
                "extraction_level": "required",
                "start_keywords": [
                    "2. Company/Name"
                ],
                "start_symbols": [],
                "end_keywords": [
                    "3. Legal form"
                ],
                "end_symbols": [],
                "regex": "",
                "preprocessing": null,
                "postprocessing": "standardize_company_name"
            }
        }
    }
}
```

## Adding a New Document Type or Language
To add a new document type or language:
1. **Modify the configuration file**: Add a new section for the document type or language inside `services/documents_settings`
2. **Implement a new parser class**: Create a parser class inside `services/pdf_parsers/`.
3. **Register the parser**: Ensure the new parser is selectable in the `parse()` method of `ParserManager`.

## Template Filling (DOCX)
- Placeholders in the template correspond to field names in the configuration.
- Placeholders must be enclosed in double curly brackets `{{}}`.
- Insert placeholders as plain text to avoid formatting issues.
- If a field contains multiple values (e.g., a list of extracted data), each value is inserted at the corresponding placeholder in the template. If a placeholder appears within a paragraph, the entire block of paragraphs is duplicated for each value. The duplication is confined within the boundaries of the nearest headings, ensuring that repeated content remains structured and contextually relevant.
---
This system provides a structured and flexible way to extract and process document data efficiently.

