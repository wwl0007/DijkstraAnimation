# Wesley Lowman
# COMP 5970
# Manim Animation Project

from manim import *

import networkx as nx

import random

class Run(Scene):

    def construct(self):
        # Create a default graph in networkx
        G = nx.Graph()
        # Add nodes to the graph
        #G.add_nodes_from([node for node in "abcdef", {'cost': 0}]) Try to get this working ASAP
        G.add_nodes_from([('a', {'cost': float('inf')})])
        G.add_nodes_from([('b', {'cost': float('inf')})])
        G.add_nodes_from([('c', {'cost': float('inf')})])
        G.add_nodes_from([('d', {'cost': float('inf')})])
        G.add_nodes_from([('e', {'cost': float('inf')})])
        G.add_nodes_from([('f', {'cost': float('inf')})])
        # Add edges between the nodes in the graph
        G.add_edge("a","b", weight=17)
        G.add_edge("a","c", weight=12)
        G.add_edge("a","d", weight=8)
        G.add_edge("b","c", weight=1)
        G.add_edge("b","e", weight=6)
        G.add_edge("c","d", weight=7)
        G.add_edge("c","f", weight=11)
        G.add_edge("d","f", weight=15)
        G.add_edge("e","f", weight=5)
        # Declare the source node; it can be changed using the line below as needed
        source_node = "a"
        # Create a table used to track the lowest possible cost from the source node to another node
        table = Table(
            [[str(G.nodes["a"]["cost"])],[str(G.nodes["b"]["cost"])], [str(G.nodes["c"]["cost"])], [str(G.nodes["d"]["cost"])], [str(G.nodes["e"]["cost"])], [str(G.nodes["f"]["cost"])]],
            row_labels=[Text("A"), Text("B"), Text("C"), Text("D"), Text("E"), Text("F")],
            col_labels=[Text("Cost")],
            top_left_entry=Text("Node"),
            include_outer_lines=True).scale(0.7)
        # Convert the networkx graph elements to manim graph elements
        vertices = list(G.nodes)
        edges = list(G.edges)
        # Construct the manim graph
        graph = Graph(vertices, edges, layout="spring", layout_scale=3, labels=True, root_vertex="None").scale(1.2)
        # Group the table and graph together for animation purposes
        g = Group(
            table, graph
        ).arrange_in_grid(buff=1)
        # Create and position the table and graph that will be used in this animation
        self.play(table.create())
        self.play(Create(graph, run_time = 5))
        self.play(graph.animate.shift(0.35 * RIGHT))
        # PAUSE FOR NOW

        graph[(source_node)].fill_color = RED
        graph[(source_node)].fill_color = YELLOW
        #self.play(graph[(source_node)].animate.set_color(BLUE))
        self.play(graph.edges[("a", "b")].animate.set_color(RED), run_time = 3)

        # Table Test
        node_a = table.get_entries((2,1)).set_color(BLUE)
        node_b = table.get_entries((3,1)).set_color(BLUE)
        node_c = table.get_entries((4,1)).set_color(BLUE)
        node_d = table.get_entries((5,1)).set_color(BLUE)
        node_e = table.get_entries((6,1)).set_color(BLUE)
        node_f = table.get_entries((7,1)).set_color(BLUE)

        #source_node set color
        #current_node set color

        self.play(Transform(node_a, Text("D").scale(0.7).move_to(node_a).set_color(node_a.get_color())))
        self.play(Transform(node_b, Text("C").scale(0.7).move_to(node_b).set_color(node_b.get_color())))
        self.play(Transform(node_c, Text("Z").scale(0.7).move_to(node_c).set_color(node_c.get_color())))
        self.play(Transform(node_d, Text("W").scale(0.7).move_to(node_d).set_color(node_d.get_color())))

        G.nodes["a"]["cost"] = 22
        #self.play(ReplacementTransform(node_a, Text(str(G.nodes["a"]["cost"])).scale(0.7).move_to(node_a).set_color(node_a.get_color())))
        self.loopTest("WesleyWatson", node_a, G.nodes["a"]["cost"])

        # Initiate a wait process to ensure the animation finishes as intended
        self.wait()

    def loopTest(self, word, nodeChosen, cost):
        wordTest = word
        for letter in wordTest:
            cost = random.randint(0, 9)
            self.play(Transform(nodeChosen, Text(str(cost)).scale(0.7).move_to(nodeChosen).set_color(nodeChosen.get_color())))
