import networkx as nx

from src.visualiser import GraphVisualiser


graph = nx.Graph()


graph.add_node(
    "process",
    importance=0.9,
    community=0
)

graph.add_node(
    "memory",
    importance=0.8,
    community=0
)

graph.add_node(
    "kernel",
    importance=0.7,
    community=0
)

graph.add_node(
    "tcp",
    importance=0.6,
    community=1
)

graph.add_node(
    "ip",
    importance=0.5,
    community=1
)


graph.add_edge(
    "process",
    "memory",
    weight=5
)

graph.add_edge(
    "process",
    "kernel",
    weight=3
)

graph.add_edge(
    "tcp",
    "ip",
    weight=4
)


visualizer = GraphVisualiser()

output = visualizer.create_graph(
    graph,
    "generated/test_graph.html"
)


print(
    f"Graph created at: {output}"
)