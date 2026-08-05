import re

import spacy


nlp = spacy.load("en_core_web_sm")


class TextPreprocessor:
    """
    Cleans lecture notes and prepares them for NLP analysis.
    """

    def clean(self, text: str) -> str:
        """
        Clean a piece of text and return the result.
        """

        text = text.lower()

        text = re.sub(
            r"http\S+",
            "",
            text
        )

        text = re.sub(
            r"\d+",
            " ",
            text
        )

        text = re.sub(
            r"[^a-z\s]",
            " ",
            text
        )

        text = re.sub(
            r"\s+",
            " ",
            text
        ).strip()

        doc = nlp(text)

        cleaned_words = []

        for token in doc:

            if token.is_stop:
                continue

            if token.is_space:
                continue

            if not token.is_alpha:
                continue

            lemma = token.lemma_.strip()

            if len(lemma) < 2:
                continue

            cleaned_words.append(lemma)

        return " ".join(cleaned_words)