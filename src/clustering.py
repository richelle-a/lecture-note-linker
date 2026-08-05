import community as community_louvain
import networkx as nx


class CommunityDetector:
    """
    Detects communities within the knowledge graph
    using the Louvain algorithm.
    """

    def detect(self, graph):
        """
        Detect communities and return a dictionary.

        Example:

        {
            "process": 0,
            "memory": 0,
            "kernel": 0,
            "tcp": 1,
            "udp": 1
        }
        """

        if graph.number_of_nodes() == 0:
            return {}

        if graph.number_of_edges() == 0:
            return {
                node: index
                for index, node
                in enumerate(graph.nodes)
            }

        partition = community_louvain.best_partition(
            graph,
            weight="weight"
        )

        return partition

    def add_communities_to_graph(self, graph):
        """
        Detect communities and store the community
        number as an attribute on each node.
        """

        partition = self.detect(graph)

        nx.set_node_attributes(
            graph,
            partition,
            "community"
        )

        return graph