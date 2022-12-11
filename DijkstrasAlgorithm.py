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

        color_vertex("a", RED)
        color_edge(("a, b"), RED)
        change_cell_text(cost_a_table_cell, 0, WHITE)

        # Initiate a wait process to ensure the animation finishes as intended
        self.wait()

    # CUSTOM ANIMATION FUNCTIONS
    def color_vertex(self, vertex, color):
        self.play(
            graph[(vertex)][0].animate.set_color(color),
            graph[(vertex)][1].animate.set_color(BLACK),
            runtime=3
        )

    def color_edge(self, edge, color):
        self.play(graph.edges[edge].animate.set_color(color), run_time = 2)

    def change_cell_text(self, cell, text, color):
        self.play(Transform(cell, Text(text).scale(0.7).move_to(cell).set_color(color)))

        '''
        OLD CODE
        #source_node set color
        #current_node set color
        self.play(Transform(node_a, Text("D").scale(0.7).move_to(node_a).set_color(node_a.get_color())))
        self.play(Transform(node_b, Text("C").scale(0.7).move_to(node_b).set_color(node_b.get_color())))
        self.play(Transform(node_c, Text("Z").scale(0.7).move_to(node_c).set_color(node_c.get_color())))
        self.play(Transform(node_d, Text("W").scale(0.7).move_to(node_d).set_color(node_d.get_color())))

        G.nodes["a"]["cost"] = 22
        #self.play(ReplacementTransform(node_a, Text(str(G.nodes["a"]["cost"])).scale(0.7).move_to(node_a).set_color(node_a.get_color())))
        self.loopTest("WesleyWatson", node_a, G.nodes["a"]["cost"])



    def loopTest(self, word, nodeChosen, cost):
        wordTest = word
        for letter in wordTest:
            cost = random.randint(0, 9)
            self.play(Transform(nodeChosen, Text(str(cost)).scale(0.7).move_to(nodeChosen).set_color(nodeChosen.get_color())))

    OLD ANIMATION CODE 1
    self.play(
        graph[("a")][0].animate.set_color(RED),
        graph[("a")][1].animate.set_color(BLACK),
        runtime=3
    )
    self.play(graph.edges[("a", "b")].animate.set_color(RED), run_time = 2.5)



    # Change source node cost table value
    self.play(Transform(cost_a_table_cell, Text("0").scale(0.7).move_to(cost_a_table_cell).set_color(cost_a_table_cell.get_color())))
            '''
