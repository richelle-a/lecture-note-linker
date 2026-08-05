from pathlib import Path

from flask import (
    Flask,
    render_template,
    request,
    send_from_directory
)

from src.file_loader import FileLoader
from src.preprocessing import TextPreprocessor
from src.tfidf import TfidfExtractor
from src.graph_builder import KnowledgeGraphBuilder
from src.clustering import CommunityDetector
from src.visualiser import GraphVisualiser


app = Flask(__name__)


UPLOAD_FOLDER = Path("uploads")

GENERATED_FOLDER = Path("generated")


UPLOAD_FOLDER.mkdir(
    exist_ok=True
)

GENERATED_FOLDER.mkdir(
    exist_ok=True
)


loader = FileLoader()

preprocessor = TextPreprocessor()

tfidf_extractor = TfidfExtractor(
    max_features=30
)

graph_builder = KnowledgeGraphBuilder(
    window_size=5
)

community_detector = CommunityDetector()

visualiser = GraphVisualiser()


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/upload",
    methods=["POST"]
)
def upload():

    file = request.files.get("notes")

    if not file or file.filename == "":
        return "No file selected."

    filepath = UPLOAD_FOLDER / file.filename

    file.save(filepath)


    # Load notes

    raw_text = loader.load(
        filepath
    )


    # Preprocess

    cleaned_text = preprocessor.clean(
        raw_text
    )


    # TF-IDF

    concepts = tfidf_extractor.extract(
        [cleaned_text]
    )


    # Build graph

    graph_builder.add_concepts(
        concepts
    )

    graph = graph_builder.build_relationships(
        cleaned_text,
        concepts
    )


    # Community detection

    graph = community_detector.add_communities_to_graph(
        graph
    )


    # Generate interactive graph

    visualiser.create_graph(
        graph,
        GENERATED_FOLDER / "graph.html"
    )


    return render_template(
        "graph.html"
    )


@app.route(
    "/generated/<path:filename>"
)
def generated_file(filename):

    return send_from_directory(
        GENERATED_FOLDER,
        filename
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )