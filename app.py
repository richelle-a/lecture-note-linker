from pathlib import Path

from flask import Flask, render_template, request

from src.file_loader import FileLoader
from src.preprocessing import TextPreprocessor
from src.tfidf import TfidfExtractor
from src.graph_builder import KnowledgeGraphBuilder

app = Flask(__name__)


UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)


loader = FileLoader()

preprocessor = TextPreprocessor()

tfidf_extractor = TfidfExtractor(
    max_features=30
)

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files.get("notes")

    if not file:

        return "No file selected."

    filepath = UPLOAD_FOLDER / file.filename

    file.save(filepath)

    raw_text = loader.load(filepath)

    cleaned_text = preprocessor.clean(raw_text)

    concepts = tfidf_extractor.extract(
        [cleaned_text]
    )

    return render_template(
        "concepts.html",
        concepts=concepts
    )

if __name__ == "__main__":
    app.run(debug=True)


graph_builder = KnowledgeGraphBuilder(
    window_size=5
)