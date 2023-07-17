import networkx as nx
from manim import *
from manim_weighted_line import *


# In the graph below you can see how to add the weight to each
# edge from the networkx graph.
class PartiteGraph(Scene):
    def construct(self):
        G = nx.Graph()
        G.add_nodes_from([0, 1, 2, 3])
        G.add_weighted_edges_from([(0, 2, 500), (0, 3, 0), (1, 2, 2)])
        opts = {
            "weight_config": {
                "fill_color": BLUE,
                "fill_opacity": 1,
                "font_size": DEFAULT_FONT_SIZE * 0.75,
            },
            "weight_alpha": 0.3,
        }
        edge_conf = {(u, v): G.get_edge_data(u, v) for u, v in G.edges}
        {v.update(opts) for v in edge_conf.values()}
        graph = Graph(
            list(G.nodes),
            list(G.edges),
            layout="partite",
            partitions=[[0, 1]],
            labels=True,
            edge_type=WeightedLine,
            edge_config=edge_conf,
        )

        self.play(FadeIn(graph), run_time=2)


# In the custom di-graph below one of the edges has the
# weight configured showing the use of the main config
# options including: alpha, weight_cofig & bg_config dicts
class CustomDiGraph(Scene):
    def construct(self):
        vertices = [i for i in range(5)]
        edges = [
            (0, 1),
            (1, 2),
            (3, 2),
            (3, 4),
        ]

        edge_config = {
            "stroke_width": 2,
            "tip_config": {
                "tip_shape": ArrowSquareTip,
                "tip_length": 0.15,
            },
            (3, 4): {
                "color": RED,
                "tip_config": {"tip_length": 0.25, "tip_width": 0.25},
                "weight": 10,
                "weight_alpha": 0.9,
                "weight_config": {"color": RED},
                "bg_config": {"color": WHITE},
            },
            "weight_config": {
                "fill_color": BLACK,
                "fill_opacity": 1,
            },
            "bg_config": {
                "color": WHITE,
            },
        }

        g = DiGraph(
            vertices,
            edges,
            labels=True,
            layout="circular",
            edge_type=WeightedLine,
            edge_config=edge_config,
        ).scale(1.4)

        # self.add(g)
        self.play(Create(g))
        # self.wait()


# In the moving di-graph below you can see how to add weights to
# edges enmasse and then have them disply as the scene is animated
class MovingDiGraph(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        weights = [5, 3, 6, 11, 1]
        edge_weights = {e[0]: {"weight": e[1]} for e in zip(edges, weights)}
        g = DiGraph(
            vertices,
            edges,
            edge_type=WeightedLine,
            edge_config=edge_weights,
        )

        self.add(g)
        self.play(
            g[1].animate.move_to([1, 1, 1]),
            g[2].animate.move_to([-1, 1, 2]),
            g[3].animate.move_to([1, -1, -1]),
            g[4].animate.move_to([-1, -1, 0]),
        )
        self.wait()
