from pathlib import Path

from PyPDF2 import PdfReader
from docx import Document


class FileLoader:
    """
    Loads lecture notes from different file formats.
    """

    def load(self, filepath):

        path = Path(filepath)

        suffix = path.suffix.lower()

        if suffix == ".txt":
            return self._load_txt(path)

        elif suffix == ".pdf":
            return self._load_pdf(path)

        elif suffix == ".docx":
            return self._load_docx(path)

        else:
            raise ValueError(
                f"Unsupported file type: {suffix}"
            )

    def _load_txt(self, path):

        with open(path, "r", encoding="utf-8") as file:
            return file.read()

    def _load_pdf(self, path):

        reader = PdfReader(path)

        text = ""

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        return text

    def _load_docx(self, path):

        document = Document(path)

        text = ""

        for paragraph in document.paragraphs:

            text += paragraph.text + "\n"

        return text