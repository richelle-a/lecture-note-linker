from sklearn.feature_extraction.text import TfidfVectorizer


class TfidfExtractor:
    """
    Extracts important concepts from lecture notes using TF-IDF.
    """

    def __init__(self, max_features=50):
        """
        Create a TF-IDF vectorizer.

        max_features controls the maximum number
        of concepts we want to extract.
        """

        self.vectorizer = TfidfVectorizer(
            max_features=max_features
        )

    def extract(self, documents):
        """
        Extract important concepts from a list of documents.

        Returns a list of tuples:

        [
            ("concept", score),
            ("another concept", score)
        ]
        """

        if not documents:
            return []

        matrix = self.vectorizer.fit_transform(documents)

        feature_names = self.vectorizer.get_feature_names_out()

        scores = matrix.sum(axis=0).A1

        concepts = list(
            zip(feature_names, scores)
        )

        concepts.sort(
            key=lambda x: x[1],
            reverse=True
        )

        return concepts