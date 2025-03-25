import re


class Extractor:

    @staticmethod
    def extract_using_re(text: str, regex: str) -> list | None:
        """Extracts data from text using a regular expression."""
        if not text:
            return text
        matches = re.findall(regex, text)
        return matches if matches else None

    @staticmethod
    def extract_between_symbols(text: str, start_symbol: str, end_symbol: str) -> str | None:
        """
        Extracts data between two symbols (e.g., markers).
        """
        if not text:
            return text
        match = re.search(rf"{re.escape(start_symbol)}(.*?){re.escape(end_symbol)}", text, re.DOTALL)
        if match:
            return match.group(1).strip()
        return None

    @staticmethod
    def extract_from_start_to_end(text: str, start_keyword: str, end_keyword: str) -> str | None:
        """
        Extracts text between two keywords (e.g., start and end of a data block).
        """
        if not text:
            return text
        start_pos = text.find(start_keyword)
        if start_pos == -1:
            return None
        end_pos = text.find(end_keyword, start_pos)
        if end_pos == -1:
            return None
        return text[start_pos + len(start_keyword):end_pos].strip()

    @staticmethod
    def extract_between_keywords(text: str, start_keywords: list, end_keywords: list) -> list:
        """
        Extracts text between corresponding pairs of keywords.
        """
        if not text:
            return text
        extracted = []

        for start_keyword, end_keyword in zip(start_keywords, end_keywords):
            start_pos = 0

            while True:
                start_pos = text.find(start_keyword, start_pos)
                if start_pos == -1:
                    break

                end_pos = text.find(end_keyword, start_pos + len(start_keyword))
                if end_pos == -1:
                    break

                extracted.append(text[start_pos + len(start_keyword):end_pos].strip())
                start_pos = end_pos + len(end_keyword)

        return extracted
        # for start_keyword, end_keyword in zip(start_keywords, end_keywords):
        #     start_pos = text.find(start_keyword)
        #     if start_pos == -1:
        #         continue
        #
        #     end_pos = text.find(end_keyword, start_pos + len(start_keyword))
        #     if end_pos == -1:
        #         continue
        #
        #     extracted.append(text[start_pos + len(start_keyword):end_pos].strip())
        #
        # return extracted

    @staticmethod
    def remove_keywords(text: str, remove_keywords: list):
        """
        Removes keywords from the text.
        """
        if not text:
            return text
        for keyword in remove_keywords:
            text = text.replace(keyword, "")
        return text.strip()

    def extract_by_custom_logic(self, text: str, start_substring: str, end_substring: str = None,
                                remove_keywords: list = None):
        """
        A method for extracting text based on a custom logic (by substrings), with the option to remove keywords.
        """
        extracted_text = self.extract_from_start_to_end(text, start_substring, end_substring)
        return self.remove_keywords(extracted_text, remove_keywords) if extracted_text is not None else ""

