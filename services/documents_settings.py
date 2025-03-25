settings = {
    "registry_certificate": {
        "languages": {
            "en": {
                "markers": {
                    "meta_title": "EPZEUS",
                    "title": "EPZEUS",
                    "keywords": [
                        "EPZEUS",
                        "Commercial register and register of non-profit legal"
                    ],
                },
                "document_preprocessing": "prepare_text",
                "fields": {
                    "legal_business_name": {
                        "enabled": True,
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
                        "preprocessing": None,
                        "postprocessing": "standardize_company_name"
                    },
                    "trading_name": {
                        "enabled": True,
                        "extraction_level": "not_required",
                        "start_keywords": [
                            "Trading Name",
                            "Business Alias",
                            "Doing Business As"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "standardize_company_name"
                    },
                    "business_registration_number": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "1. UIC/PIC",
                        ],
                        "start_symbols": [],
                        "end_keywords": [
                            "2. Company/Name"
                        ],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "format_registration_number"
                    },
                    "date_incorporation": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Date of Incorporation",
                            "Company Formation Date",
                            "Registration Date"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "format_date_iso"
                    },
                    "country_incorporation": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Country of Incorporation",
                            "Registered Country",
                            "Jurisdiction"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "standardize_country_code"
                    },
                    "legal_business_address": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "5. Head office and registered office",
                        ],
                        "start_symbols": [],
                        "end_keywords": ["6. Scope of business activity"],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "clean_address"
                    },
                    "operating_address": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Operating Address",
                            "Business Premises",
                            "Physical Location"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "format_address"
                    },
                    "business_website_url": {
                        "enabled": True,
                        "extraction_level": "recommended",
                        "start_keywords": [
                            "Company Website",
                            "Official Website",
                            "Business URL"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "normalize_url"
                    },
                    "business_email": {
                        "enabled": True,
                        "extraction_level": "recommended",
                        "start_keywords": [
                            "Company Email",
                            "Official Email",
                            "Business Contact Email"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "normalize_email"
                    },
                    "business_phone_number": {
                        "enabled": True,
                        "extraction_level": "recommended",
                        "start_keywords": [
                            "Company Phone Number",
                            "Business Contact Number",
                            "Telephone"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "format_phone_number"
                    },
                    "business_entity": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "3. Legal form",
                        ],
                        "start_symbols": [],
                        "end_keywords": [
                            "4. Transcription in a foreign language"
                        ],
                        "end_symbols": [],
                        "preprocessing": "normalize_entity_type",
                        "postprocessing": "standardize_entity_type"
                    },
                    "director_full_name": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "7. Managers"
                        ],
                        "start_symbols": [],
                        "end_keywords": ["11. Manner of representation"],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "split_directors_names"
                    },
                    "director_residential_address": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Director’s Residential Address",
                            "Home Address",
                            "Private Address"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "split_directors_addresses"
                    }
                }
            },
            "bg": {
                "markers": {
                    "meta_title": "ЕПЗЕУ",
                    "title": "ЕПЗЕУ",
                    "keywords": [
                        "ЕПЗЕУ",
                        "Търговски регистър и регистър на юридическите лица"
                    ],
                },
                "document_preprocessing": "prepare_text",
                "document_postprocessing": "remove_number_from_end",
                "fields": {
                    "legal_business_name": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "2. Фирма/Наименование"
                        ],
                        "start_symbols": [],
                        "end_keywords": [
                            "3. Правна форма"
                        ],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": ["remove_number_from_end"]
                    },
                    "trading_name": {
                        "enabled": True,
                        "extraction_level": "not_required",
                        "start_keywords": [
                            "Trading Name",
                            "Business Alias",
                            "Doing Business As"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": ["remove_number_from_end"]
                    },
                    "business_registration_number": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "1. ЕИК/ПИК",
                        ],
                        "start_symbols": [],
                        "end_keywords": [
                            "2. Фирма/Наименование"
                        ],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": ["format_registration_number", "remove_number_from_end"]
                    },
                    "date_incorporation": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Date of Incorporation",
                            "Company Formation Date",
                            "Registration Date"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": ["format_date_iso", "remove_number_from_end"]
                    },
                    "country_incorporation": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Country of Incorporation",
                            "Registered Country",
                            "Jurisdiction"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": ["standardize_country_code", "remove_number_from_end"]
                    },
                    "legal_business_address": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "5. Седалище и адрес на управление",
                        ],
                        "start_symbols": [],
                        "end_keywords": ["6. Предмет на дейност"],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": ["remove_number_from_end", "clean_address"]
                    },
                    "operating_address": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Operating Address",
                            "Business Premises",
                            "Physical Location"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": ["format_address", "remove_number_from_end"]
                    },
                    "business_website_url": {
                        "enabled": True,
                        "extraction_level": "recommended",
                        "start_keywords": [
                            "Интернет страница:",
                        ],
                        "start_symbols": [],
                        "end_keywords": ["6. Предмет на дейност"],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": ["normalize_url"]
                    },
                    "business_email": {
                        "enabled": True,
                        "extraction_level": "recommended",
                        "start_keywords": [
                            "електронна поща:",
                        ],
                        "start_symbols": [],
                        "end_keywords": ["Интернет страница:"],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": ["normalize_email"]
                    },
                    "business_phone_number": {
                        "enabled": True,
                        "extraction_level": "recommended",
                        "start_keywords": [
                            "Company Phone Number",
                            "Business Contact Number",
                            "Telephone"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": ["format_phone_number", "remove_number_from_end"]
                    },
                    "business_entity": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "3. Правна форма",
                        ],
                        "start_symbols": [],
                        "end_keywords": [
                            "4. Изписване на чужд език"
                        ],
                        "end_symbols": [],
                        "preprocessing": "normalize_entity_type",
                        "postprocessing": ["standardize_entity_type", "remove_number_from_end"]
                    },
                    "director_full_name": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "7. Управители"
                        ],
                        "start_symbols": [],
                        "end_keywords": ["19. Съдружници"],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": ["remove_number_from_end", "split_directors_names", ],
                    },
                    "director_residential_address": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Director’s Residential Address",
                            "Home Address",
                            "Private Address"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": ["remove_number_from_end", "split_directors_addresses", ]
                    }
                }
            }
        }
    },
    "registro_mercantil": {
        "languages": {
            "en": {
                "markers": {
                    "meta_title": "Nota informativa",
                    "title": "Registro Mercantil",
                    "keywords": [
                        "Registro Mercantil",
                        "Interactive business information of Spanish Business Registries"
                    ],
                },
                "document_preprocessing": "prepare_text",
                "fields": {
                    "legal_business_name": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Name of company:"
                        ],
                        "start_symbols": [],
                        "end_keywords": [
                            "Start of business:"
                        ],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "standardize_company_name"
                    },
                    "trading_name": {
                        "enabled": True,
                        "extraction_level": "not_required",
                        "start_keywords": [
                            "Trading Name",
                            "Business Alias",
                            "Doing Business As"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "standardize_company_name"
                    },
                    "business_registration_number": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "NIF:",
                        ],
                        "start_symbols": [],
                        "end_keywords": [
                            "LEI code:"
                        ],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "format_registration_number"
                    },
                    "date_incorporation": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Start of business:"
                        ],
                        "start_symbols": [],
                        "end_keywords": ["Company's registered office:"],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "format_date_iso"
                    },
                    "country_incorporation": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Country of Incorporation",
                            "Registered Country",
                            "Jurisdiction"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "standardize_country_code"
                    },
                    "legal_business_address": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Company's registered office:",
                        ],
                        "start_symbols": [],
                        "end_keywords": ["Duration:"],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "clean_address"
                    },
                    "operating_address": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Operating Address",
                            "Business Premises",
                            "Physical Location"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "format_address"
                    },
                    "business_website_url": {
                        "enabled": True,
                        "extraction_level": "recommended",
                        "start_keywords": [
                            "Company Website",
                            "Official Website",
                            "Business URL"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "normalize_url"
                    },
                    "business_email": {
                        "enabled": True,
                        "extraction_level": "recommended",
                        "start_keywords": [
                            "Company Email",
                            "Official Email",
                            "Business Contact Email"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "normalize_email"
                    },
                    "business_phone_number": {
                        "enabled": True,
                        "extraction_level": "recommended",
                        "start_keywords": [
                            "Company Phone Number",
                            "Business Contact Number",
                            "Telephone"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "format_phone_number"
                    },
                    "business_entity": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "3. Legal form",
                        ],
                        "start_symbols": [],
                        "end_keywords": [
                            "4. Transcription in a foreign language"
                        ],
                        "end_symbols": [],
                        "preprocessing": None,
                        "postprocessing": None,
                    },
                    "director_full_name": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Name:"
                        ],
                        "start_symbols": [],
                        "end_keywords": ["NIF:"],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": None,
                    },
                    "director_residential_address": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Residence:"
                        ],
                        "start_symbols": [],
                        "end_keywords": ["Protocol number:"],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": None,
                    }
                }
            },
            "es": {
                "markers": {
                    "meta_title": "Nota informativa",
                    "title": "Registro Mercantil",
                    "keywords": [
                        "Registro Mercantil",
                        "Información Mercantil interactiva de los Registros Mercantiles de España"
                    ],
                },
                "document_preprocessing": "prepare_text",
                "fields": {
                    "legal_business_name": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Denominación:"
                        ],
                        "start_symbols": [],
                        "end_keywords": [
                            "Inicio de operaciones:"
                        ],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "standardize_company_name"
                    },
                    "trading_name": {
                        "enabled": True,
                        "extraction_level": "not_required",
                        "start_keywords": [
                            "Trading Name",
                            "Business Alias",
                            "Doing Business As"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "standardize_company_name"
                    },
                    "business_registration_number": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "N.I.F.:",
                        ],
                        "start_symbols": [],
                        "end_keywords": [
                            "Datos registrales:"
                        ],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "format_registration_number"
                    },
                    "date_incorporation": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Inicio de operaciones:"
                        ],
                        "start_symbols": [],
                        "end_keywords": ["Domicilio social:"],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "format_date_iso"
                    },
                    "country_incorporation": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Country of Incorporation",
                            "Registered Country",
                            "Jurisdiction"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "standardize_country_code"
                    },
                    "legal_business_address": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Domicilio social:",
                        ],
                        "start_symbols": [],
                        "end_keywords": ["Duración:"],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "clean_address"
                    },
                    "operating_address": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Operating Address",
                            "Business Premises",
                            "Physical Location"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "format_address"
                    },
                    "business_website_url": {
                        "enabled": True,
                        "extraction_level": "recommended",
                        "start_keywords": [
                            "Company Website",
                            "Official Website",
                            "Business URL"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "normalize_url"
                    },
                    "business_email": {
                        "enabled": True,
                        "extraction_level": "recommended",
                        "start_keywords": [
                            "Company Email",
                            "Official Email",
                            "Business Contact Email"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "normalize_email"
                    },
                    "business_phone_number": {
                        "enabled": True,
                        "extraction_level": "recommended",
                        "start_keywords": [
                            "Company Phone Number",
                            "Business Contact Number",
                            "Telephone"
                        ],
                        "start_symbols": [],
                        "end_keywords": [],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": "format_phone_number"
                    },
                    "business_entity": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "3. Legal form",
                        ],
                        "start_symbols": [],
                        "end_keywords": [
                            "4. Transcription in a foreign language"
                        ],
                        "end_symbols": [],
                        "preprocessing": None,
                        "postprocessing": None,
                    },
                    "director_full_name": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Nombre:"
                        ],
                        "start_symbols": [],
                        "end_keywords": ["DNI:"],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": None,
                    },
                    "director_residential_address": {
                        "enabled": True,
                        "extraction_level": "required",
                        "start_keywords": [
                            "Residencia:"
                        ],
                        "start_symbols": [],
                        "end_keywords": ["Número de protocolo:"],
                        "end_symbols": [],
                        "regex": "",
                        "preprocessing": None,
                        "postprocessing": None,
                    }
                }
            },
        }

    }
}
