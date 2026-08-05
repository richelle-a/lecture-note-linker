from src.graph_builder import KnowledgeGraphBuilder
import matplotlib.pyplot as plt
import networkx as nx


concepts = [
    ("process", 0.90),
    ("memory", 0.80),
    ("kernel", 0.70),
    ("scheduling", 0.60)
]


builder = KnowledgeGraphBuilder()

builder.add_concepts(concepts)

graph = builder.add_relationships(concepts)


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
        data
    )


pos = nx.spring_layout(graph)

nx.draw(
    graph,
    pos,
    with_labels=True,
    node_size=2000,
    font_size=10
)

plt.show()