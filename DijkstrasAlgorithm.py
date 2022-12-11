# Wesley Lowman
# COMP 5970
# Manim Animation Project

from manim import *

import networkx as nx

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
            row_labels=[Text("a"), Text("b"), Text("c"), Text("d"), Text("e"), Text("f")],
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

        # Create Arrays to Store Table Cells
        node_table_cells = []
        cost_table_cells = []

        # Create Storage Values for Node Table Cells
        node_a_table_cell = table.get_entries((2,1)).set_color(WHITE)
        node_b_table_cell = table.get_entries((3,1)).set_color(WHITE)
        node_c_table_cell = table.get_entries((4,1)).set_color(WHITE)
        node_d_table_cell = table.get_entries((5,1)).set_color(WHITE)
        node_e_table_cell = table.get_entries((6,1)).set_color(WHITE)
        node_f_table_cell = table.get_entries((7,1)).set_color(WHITE)

        # Add Node Table Cells to Storage Array
        node_table_cells.append(node_a_table_cell)
        node_table_cells.append(node_b_table_cell)
        node_table_cells.append(node_c_table_cell)
        node_table_cells.append(node_d_table_cell)
        node_table_cells.append(node_e_table_cell)
        node_table_cells.append(node_f_table_cell)

        # Create Storage Values for Cost Table Cells
        cost_a_table_cell = table.get_entries((2,2)).set_color(WHITE)
        cost_b_table_cell = table.get_entries((3,2)).set_color(WHITE)
        cost_c_table_cell = table.get_entries((4,2)).set_color(WHITE)
        cost_d_table_cell = table.get_entries((5,2)).set_color(WHITE)
        cost_e_table_cell = table.get_entries((6,2)).set_color(WHITE)
        cost_f_table_cell = table.get_entries((7,2)).set_color(WHITE)

        # Add Node Table Cells to Storage Array
        cost_table_cells.append(cost_a_table_cell)
        cost_table_cells.append(cost_b_table_cell)
        cost_table_cells.append(cost_c_table_cell)
        cost_table_cells.append(cost_d_table_cell)
        cost_table_cells.append(cost_e_table_cell)
        cost_table_cells.append(cost_f_table_cell)

        # Run the animation - comment out the animation version that you don't want to run
        # You can either run the hard-coded version or the algorithmic version
        self.play_hardcoded_animation(graph, cost_table_cells, node_table_cells)
        #self.play_algorithmic_animation(G, v graph, cost_table_cells, node_table_cells) - FUNCTIONALITY COMING SOON

        # Initiate a wait process to ensure the animation finishes as intended
        self.wait(5)

    # FULL ANIMATION FUNCTIONS
    # DIJKSTRAS ALGORITHM IMPLEMENTATION (ALGORITHMIC VERSION)

    # HARDCODED DEMONSTRATION (HARDCODED VERSION)
    def play_hardcoded_animation(self, animated_graph, cost_cell_array, node_cell_array):
        # Step 1. Source Node
        self.color_vertex(animated_graph[("a")], RED)
        self.change_cell_text(node_cell_array[0], "a", RED)
        self.change_cell_text(cost_cell_array[0], "0", RED)
        # Step 2. Travel to node d
        self.color_edge(animated_graph.edges[("a", "b")], YELLOW)
        self.color_edge(animated_graph.edges[("a", "c")], YELLOW)
        self.color_edge(animated_graph.edges[("a", "d")], YELLOW)
        self.change_cell_text(node_cell_array[1], "b", YELLOW))
        self.change_cell_text(node_cell_array[2], "c", YELLOW))
        self.change_cell_text(node_cell_array[3], "d", YELLOW))
        self.change_cell_text(cost_cell_array[1], "17", YELLOW)
        self.change_cell_text(cost_cell_array[2], "12", YELLOW)
        self.change_cell_text(cost_cell_array[3], "8", YELLOW)
        self.color_edge(animated_graph.edges[("a", "d")], GREEN)
        self.change_cell_text(cost_cell_array[3], "8", GREEN)
        self.change_cell_text(node_cell_array[3], "d", GREEN))
        self.color_vertex(animated_graph[("d")], GREEN)
        # Step 2. Travel to node d
        self.color_edge(animated_graph.edges[("c", "d")], YELLOW)
        self.color_edge(animated_graph.edges[("d", "f")], YELLOW)
        self.change_cell_text(node_cell_array[5], "f", YELLOW))
        self.change_cell_text(cost_cell_array[5], "23", YELLOW)
        self.color_edge(animated_graph.edges[("a", "c")], GREEN)
        self.change_cell_text(cost_cell_array[2], "12", GREEN)
        self.change_cell_text(node_cell_array[2], "c", GREEN))
        self.color_vertex(animated_graph[("c")], GREEN)





    # CUSTOM ANIMATION FUNCTIONS
    # Function that colors the fill of a vertex
    def color_vertex(self, vertex, color):
        self.play(
            vertex[0].animate.set_color(color),
            vertex[1].animate.set_color(BLACK),
            runtime=3
        )
    # Function that colors an edge in a graph
    def color_edge(self, edge, color):
        self.play(edge.animate.set_color(color), run_time = 1.5)

    # Function that changes the text of a cell in a table
    def change_cell_text(self, cell, text, color):
        self.play(Transform(cell, Text(text).scale(0.7).move_to(cell).set_color(color)))
