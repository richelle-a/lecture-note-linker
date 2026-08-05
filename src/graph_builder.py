from itertools import combinations

import networkx as nx


class KnowledgeGraphBuilder:
    """
    Builds a weighted knowledge graph from important concepts.
    """

    def __init__(self):
        self.graph = nx.Graph()

    def add_concepts(self, concepts):
        """
        Add concepts as nodes to the graph.

        concepts should be a list such as:

        [
            ("process", 0.82),
            ("memory", 0.71),
            ("kernel", 0.65)
        ]
        """

        for concept, score in concepts:

            self.graph.add_node(
                concept,
                importance=float(score)
            )

    def add_relationships(self, concepts):
        """
        Create weighted edges between concepts.

        Concepts appearing together are considered related.
        """

        concept_names = [
            concept
            for concept, score in concepts
        ]

        for concept_a, concept_b in combinations(
            concept_names,
            2
        ):

            if self.graph.has_edge(
                concept_a,
                concept_b
            ):

                self.graph[concept_a][concept_b]["weight"] += 1

            else:

                self.graph.add_edge(
                    concept_a,
                    concept_b,
                    weight=1
                )

        return self.graph

    def get_graph(self):
        """
        Return the NetworkX graph.
        """

        return self.graph