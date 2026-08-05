import re
import spacy

# Load the English NLP model once when the application starts.
nlp = spacy.load("en_core_web_sm")


class TextPreprocessor:
    """
    Cleans lecture notes and prepares them for analysis.
    """

    def clean(self, text: str) -> str:
        """
        Returns cleaned text as a single string.
        """

        # Convert to lowercase.
        text = text.lower()

        # Remove URLs.
        text = re.sub(r"http\S+", "", text)

        # Remove numbers.
        text = re.sub(r"\d+", " ", text)

        # Remove punctuation (keep letters and spaces).
        text = re.sub(r"[^a-z\s]", " ", text)

        # Remove extra whitespace.
        text = re.sub(r"\s+", " ", text).strip()

        # Run through spaCy.
        doc = nlp(text)

        cleaned_words = []

        for token in doc:

            if token.is_stop:
                continue

            if token.is_space:
                continue

            lemma = token.lemma_.strip()

            if len(lemma) < 2:
                continue

            cleaned_words.append(lemma)

        return " ".join(cleaned_words)