from pathlib import Path
from src.preprocessing import TextPreprocessor
from flask import Flask, render_template, request

from src.file_loader import FileLoader

app = Flask(__name__)
preprocessor = TextPreprocessor()

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)

loader = FileLoader()


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

    text = loader.load(filepath)
    cleaned_text = preprocessor.clean(text)

    return f"""
    <h2>Preprocessing Complete!</h2>
    <h3>Original Text</h3>
    <pre>{text[:500]}</pre>
    <hr>
    <h3>Cleaned Text</h3>
    <pre>{cleaned_text[:500]}</pre>
    """


if __name__ == "__main__":
    app.run(debug=True)