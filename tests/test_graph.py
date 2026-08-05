from src.graph_builder import KnowledgeGraphBuilder
import networkx as nx


concepts = [
    ("process", 0.90),
    ("memory", 0.80),
    ("kernel", 0.70),
    ("scheduling", 0.60)
]


text = """
The process requires memory to execute.

The operating system uses the kernel
to manage processes.

Process scheduling determines which
process runs next.

Memory is managed by the operating system.
"""


builder = KnowledgeGraphBuilder(
    window_size=5
)


builder.add_concepts(
    concepts
)


graph = builder.build_relationships(
    text,
    concepts
)


print("\nNodes:\n")

for node, data in graph.nodes(data=True):

    print(
        node,
        data
    )


print("\nEdges:\n")

for node_a, node_b, data in graph.edges(data=True):

    print(
        node_a,
        "<->",
        node_b,
        "weight:",
        data["weight"]
    )

import matplotlib.pyplot as plt


position = nx.spring_layout(
    graph,
    seed=42
)


nx.draw(
    graph,
    position,
    with_labels=True,
    node_size=2000
)


edge_labels = nx.get_edge_attributes(
    graph,
    "weight"
)


nx.draw_networkx_edge_labels(
    graph,
    position,
    edge_labels=edge_labels
)


plt.show()