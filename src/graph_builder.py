from itertools import combinations
import re
import networkx as nx


class KnowledgeGraphBuilder:
    """
    Builds a weighted knowledge graph based on
    concept co-occurrence within a sliding window.
    """

    def __init__(self, window_size=5):
        """
        Create an empty graph.

        window_size determines how many words we
        look at around each concept.
        """

        self.graph = nx.Graph()

        self.window_size = window_size

    def add_concepts(self, concepts):
        """
        Add important concepts as graph nodes.

        concepts should look like:

        [
            ("process", 0.82),
            ("memory", 0.71)
        ]
        """

        for concept, score in concepts:

            self.graph.add_node(
                concept,
                importance=float(score)
            )

    def build_relationships(
        self,
        text,
        concepts
    ):
        """
        Build weighted edges using concept co-occurrence.
        """

        concept_names = {
            concept.lower()
            for concept, score in concepts
        }

        text = text.lower()

        text = re.sub(
         r"[^a-z\s]",
         " ",
            text
        )

        words = text.split()
        

        for i in range(len(words)):

            window = words[
                i:i + self.window_size
            ]

            concepts_in_window = [
                word
                for word in window
                if word in concept_names
            ]

            unique_concepts = list(
                set(concepts_in_window)
            )

            for concept_a, concept_b in combinations(
                unique_concepts,
                2
            ):

                if self.graph.has_edge(
                    concept_a,
                    concept_b
                ):

                    self.graph[
                        concept_a
                    ][
                        concept_b
                    ]["weight"] += 1

                else:

                    self.graph.add_edge(
                        concept_a,
                        concept_b,
                        weight=1
                    )

        return self.graph

    def get_graph(self):
        """
        Return the graph.
        """

        return self.graph