import networkx as nx

from src.clustering import CommunityDetector


graph = nx.Graph()


# Operating Systems
graph.add_edge(
    "process",
    "memory",
    weight=5
)

graph.add_edge(
    "process",
    "kernel",
    weight=5
)

graph.add_edge(
    "memory",
    "kernel",
    weight=5
)


# Networking
graph.add_edge(
    "tcp",
    "ip",
    weight=5
)

graph.add_edge(
    "ip",
    "udp",
    weight=5
)

graph.add_edge(
    "tcp",
    "udp",
    weight=5
)


detector = CommunityDetector()

graph = detector.add_communities_to_graph(
    graph
)


print("\nNodes:\n")

for node, data in graph.nodes(data=True):

    print(
        node,
        "→",
        data
    )