from src.preprocessing import TextPreprocessor
from src.tfidf import TfidfExtractor
from src.graph_builder import KnowledgeGraphBuilder


documents = [

    """
    Processes require memory to execute.
    The operating system manages processes.
    """,

    """
    Memory management is an important operating system function.
    Processes are scheduled by the operating system.
    """,

    """
    The kernel manages processes and memory.
    Scheduling determines which process runs.
    """
]


# -------------------------
# Preprocessing
# -------------------------

preprocessor = TextPreprocessor()

cleaned_documents = []

for document in documents:

    cleaned = preprocessor.clean(
        document
    )

    cleaned_documents.append(cleaned)


# -------------------------
# TF-IDF
# -------------------------

extractor = TfidfExtractor(
    max_features=10
)

concepts = extractor.extract(
    cleaned_documents
)


print("\nImportant concepts:\n")

for concept, score in concepts:

    print(
        f"{concept:20} {score:.3f}"
    )


# -------------------------
# Graph
# -------------------------

builder = KnowledgeGraphBuilder()

builder.add_concepts(
    concepts
)

graph = builder.add_relationships(
    concepts
)


print("\nGraph:\n")

print(
    "Nodes:",
    graph.number_of_nodes()
)

print(
    "Edges:",
    graph.number_of_edges()
)