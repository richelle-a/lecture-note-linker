from src.preprocessing import TextPreprocessor
from src.tfidf import TfidfExtractor
from src.graph_builder import KnowledgeGraphBuilder
from src.clustering import CommunityDetector


documents = [

    """
    Processes require memory to execute.
    The operating system manages processes.
    Process scheduling determines execution.
    The kernel manages memory.
    """,

    """
    Computer networks transmit packets.
    TCP provides reliable communication.
    UDP provides fast communication.
    IP routes packets across networks.
    """
]


# --------------------------------
# 1. Preprocessing
# --------------------------------

preprocessor = TextPreprocessor()

cleaned_documents = []

for document in documents:

    cleaned_documents.append(
        preprocessor.clean(document)
    )


# --------------------------------
# 2. TF-IDF
# --------------------------------

extractor = TfidfExtractor(
    max_features=15
)

concepts = extractor.extract(
    cleaned_documents
)


print("\nConcepts:\n")

for concept, score in concepts:

    print(
        f"{concept:20} {score:.3f}"
    )


# --------------------------------
# 3. Build graph
# --------------------------------

builder = KnowledgeGraphBuilder(
    window_size=5
)

builder.add_concepts(
    concepts
)


combined_text = " ".join(
    cleaned_documents
)


graph = builder.build_relationships(
    combined_text,
    concepts
)


# --------------------------------
# 4. Detect communities
# --------------------------------

detector = CommunityDetector()

graph = detector.add_communities_to_graph(
    graph
)


# --------------------------------
# 5. Print results
# --------------------------------

print("\nGraph nodes:\n")

for node, data in graph.nodes(data=True):

    print(
        node,
        "→",
        data
    )


print("\nGraph edges:\n")

for node_a, node_b, data in graph.edges(data=True):

    print(
        node_a,
        "<->",
        node_b,
        "weight:",
        data["weight"]
    )