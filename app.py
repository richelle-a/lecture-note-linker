from pathlib import Path

from flask import Flask, render_template, request

from src.file_loader import FileLoader

app = Flask(__name__)

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

    return f"""
    <h2>File Loaded Successfully!</h2>

    <h3>Preview:</h3>

    <pre>{text[:1500]}</pre>
    """


if __name__ == "__main__":
    app.run(debug=True)