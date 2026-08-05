from pathlib import Path

from pyvis.network import Network


class GraphVisualiser:
    """
    Converts a NetworkX knowledge graph into
    an interactive PyVis graph.
    """

    def __init__(self):
        self.network = Network(
            height="750px",
            width="100%",
            bgcolor="#0f172a",
            font_color="white",
            directed=False
        )

        self.network.set_options("""
        {
          "nodes": {
            "shape": "dot",
            "font": {
              "size": 18
            },
            "borderWidth": 2
          },

          "edges": {
            "smooth": {
              "type": "dynamic"
            }
          },

          "physics": {
            "enabled": true,
            "barnesHut": {
              "gravitationalConstant": -3000,
              "centralGravity": 0.2,
              "springLength": 150,
              "springConstant": 0.04,
              "damping": 0.09
            },

            "stabilization": {
              "iterations": 150
            }
          },

          "interaction": {
            "hover": true,
            "navigationButtons": true,
            "zoomView": true,
            "dragView": true
          }
        }
        """)

    def create_graph(self, graph, output_path):
        """
        Convert a NetworkX graph into an interactive HTML file.
        """

        community_colours = [
            "#8b5cf6",
            "#06b6d4",
            "#22c55e",
            "#f59e0b",
            "#ef4444",
            "#ec4899",
            "#3b82f6"
        ]

        for node, data in graph.nodes(data=True):

            importance = data.get(
                "importance",
                0.1
            )

            community = data.get(
                "community",
                0
            )

            colour = community_colours[
                community % len(community_colours)
            ]

            size = 15 + (
                importance * 40
            )

            self.network.add_node(
                node,
                label=node,
                title=(
                    f"<b>{node}</b><br>"
                    f"Importance: {importance:.3f}<br>"
                    f"Community: {community}"
                ),
                size=size,
                color=colour
            )

        for node_a, node_b, data in graph.edges(
            data=True
        ):

            weight = data.get(
                "weight",
                1
            )

            self.network.add_edge(
                node_a,
                node_b,
                value=weight,
                title=f"Relationship strength: {weight}"
            )

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.network.write_html(
            str(output_path),
            open_browser=False
        )

        return output_path