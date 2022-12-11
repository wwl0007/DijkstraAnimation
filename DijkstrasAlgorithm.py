# Wesley Lowman
# COMP 5970
# Manim Animation Project

from manim import *

import networkx as nx

import random

class Run(Scene):
    # CONSTRUCTION CODE
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
        table = MobjectTable(
            [[MathTex("\infty")],[MathTex("\infty")], [MathTex("\infty")], [MathTex("\infty")], [MathTex("\infty")], [MathTex("\infty")]],
            row_labels=[Text("A"), Text("B"), Text("C"), Text("D"), Text("E"), Text("F")],
            col_labels=[Text("Cost")],
            top_left_entry=Text("Node"),
            include_outer_lines=True).scale(0.7)
        # Convert the networkx graph elements to manim graph elements
        vertices = list(G.nodes)
        edges = list(G.edges)
        # Construct the manim graph
        graph = Graph(vertices, edges, layout="spring", layout_scale=3, labels=True, root_vertex="None").scale(1.2)
        # Create and position edge labels for the graph
        for edge in edges:
            graph.edges[edge].set_color(BLUE)
            edge_label_value = G.edges[edge]['weight']
            edge_label = MathTex(edge_label_value, color=WHITE).scale(0.7).shift(
                [0,0.25,0]
            ).rotate(
                graph.edges[(edge[0],edge[1])].get_angle()+PI, about_point=ORIGIN
            ).shift(graph.edges[(edge[0],edge[1])].get_center())
            graph.add(edge_label)
        # Group the table and graph together for animation purposes
        g = Group(
            table, graph
        ).arrange_in_grid(buff=1)

        # Create and position the table and graph that will be used in this animation
        self.play(table.create())
        self.play(Create(graph, run_time = 5))
        self.play(graph.animate.shift(0.35 * RIGHT))

        # Create Storage Values for Node Table Cells
        node_a_table_cell = table.get_entries((2,1)).set_color(WHITE)
        node_b_table_cell = table.get_entries((3,1)).set_color(WHITE)
        node_c_table_cell = table.get_entries((4,1)).set_color(WHITE)
        node_d_table_cell = table.get_entries((5,1)).set_color(WHITE)
        node_e_table_cell = table.get_entries((6,1)).set_color(WHITE)
        node_f_table_cell = table.get_entries((7,1)).set_color(WHITE)

        # Create Storage Values for Cost Table Cells
        cost_a_table_cell = table.get_entries((2,2)).set_color(WHITE)
        cost_b_table_cell = table.get_entries((3,2)).set_color(WHITE)
        cost_c_table_cell = table.get_entries((4,2)).set_color(WHITE)
        cost_d_table_cell = table.get_entries((5,2)).set_color(WHITE)
        cost_e_table_cell = table.get_entries((6,2)).set_color(WHITE)
        cost_f_table_cell = table.get_entries((7,2)).set_color(WHITE)

        # ANIMATION RUN CODE

        self.color_vertex(graph[("a")], RED)
        self.color_edge(graph.edges[("a", "b")], RED)
        self.change_cell_text(cost_a_table_cell, "0", WHITE)

        # Initiate a wait process to ensure the animation finishes as intended
        self.wait(5)

    # CUSTOM ANIMATION FUNCTIONS
    def color_vertex(self, vertex, color):
        self.play(
            vertex[0].animate.set_color(color),
            vertex[1].animate.set_color(BLACK),
            runtime=3
        )

    def color_edge(self, edge, color):
        self.play(edge.animate.set_color(color), run_time = 1.5)

    def change_cell_text(self, cell, text, color):
        self.play(Transform(cell, Text(text).scale(0.7).move_to(cell).set_color(color)))
