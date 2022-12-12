# Wesley Lowman
# COMP 5970
# Manim Animation Project
# Original Psuedocode for IPQ and Dijkstra's algorithm created by Dr. Haynes Heaton
# Implementation code for IPQ created by Dr. Haynes Heaton

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
        G.add_edge("b","e", weight=4)
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
        self.play_hardcoded_animation(G, graph, cost_table_cells, node_table_cells)
        #self.play_algorithmic_animation(G, v graph, cost_table_cells, node_table_cells) - FUNCTIONALITY COMING SOON

        # Initiate a wait process to ensure the animation finishes as intended
        self.wait(5)

    # FULL ANIMATION FUNCTIONS
    # DIJKSTRAS ALGORITHM IMPLEMENTATION (ALGORITHMIC VERSION)

    # HARDCODED DEMONSTRATION (HARDCODED VERSION)
    def play_hardcoded_animation(self, network_x_graph, animated_graph, cost_cell_array, node_cell_array):
        # Step 0. Initialize Animation Parameters
        edge_change_run_time = 1.75
        vertex_change_run_time = 1.75
        # Step 1. Source Node
        network_x_graph.nodes["a"]["cost"] = 0
        self.play(
            self.color_vertex(animated_graph[("a")], RED),
            self.color_vertex_label(animated_graph[("a")], BLACK),
            run_time=vertex_change_run_time
        )
        self.play(self.change_cell_text(node_cell_array[0], "a", RED))
        self.play(self.change_cell_text(cost_cell_array[0], str(network_x_graph.nodes["a"]["cost"]), RED))
        # Step 2. Travel to node d
        network_x_graph.nodes["b"]["cost"] = 17
        self.play(
            self.color_edge(animated_graph.edges[("a", "b")], YELLOW),
            self.change_cell_text(node_cell_array[1], "b", YELLOW),
            self.change_cell_text(cost_cell_array[1], "17", YELLOW),
            run_time=edge_change_run_time
        )
        network_x_graph.nodes["c"]["cost"] = 12
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], YELLOW),
            self.change_cell_text(node_cell_array[2], "c", YELLOW),
            self.change_cell_text(cost_cell_array[2], "12", YELLOW),
            run_time=edge_change_run_time
        )
        network_x_graph.nodes["d"]["cost"] = 8
        self.play(
            self.color_edge(animated_graph.edges[("a", "d")], YELLOW),
            self.change_cell_text(node_cell_array[3], "d", YELLOW),
            self.change_cell_text(cost_cell_array[3], "8", YELLOW),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("a", "d")], PINK),
            self.change_cell_text(cost_cell_array[3], "8", PINK),
            self.change_cell_text(node_cell_array[3], "d", PINK),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_vertex(animated_graph[("d")], PINK),
            self.color_vertex_label(animated_graph[("d")], BLACK),
            run_time=vertex_change_run_time
        )
        # Step 3. Travel to node c
        self.play(
            self.color_edge(animated_graph.edges[("c", "d")], YELLOW),
            run_time=edge_change_run_time
        )
        network_x_graph.nodes["f"]["cost"] = 23
        self.play(
            self.color_edge(animated_graph.edges[("d", "f")], YELLOW),
            self.change_cell_text(node_cell_array[5], "f", YELLOW),
            self.change_cell_text(cost_cell_array[5], "23", YELLOW),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("a", "d")], GREEN),
            self.change_cell_text(cost_cell_array[3], "8", GREEN),
            self.change_cell_text(node_cell_array[3], "d", GREEN),
            self.color_vertex(animated_graph[("d")], GREEN),
            self.color_vertex_label(animated_graph[("d")], BLACK),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], PINK),
            self.change_cell_text(cost_cell_array[2], "12", PINK),
            self.change_cell_text(node_cell_array[2], "c", PINK),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_vertex(animated_graph[("c")], PINK),
            self.color_vertex_label(animated_graph[("c")], BLACK),
            run_time=vertex_change_run_time
        )
        # Step 4. Travel to node b
        network_x_graph.nodes["b"]["cost"] = 13
        self.play(
            self.color_edge(animated_graph.edges[("b", "c")], YELLOW),
            self.change_cell_text(cost_cell_array[1], "13", YELLOW),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("c", "f")], YELLOW),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], GREEN),
            self.change_cell_text(cost_cell_array[2], "12", GREEN),
            self.change_cell_text(node_cell_array[2], "c", GREEN),
            self.color_vertex(animated_graph[("c")], GREEN),
            self.color_vertex_label(animated_graph[("c")], BLACK),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], PINK),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("b", "c")], PINK),
            self.change_cell_text(cost_cell_array[1], "13", PINK),
            self.change_cell_text(node_cell_array[1], "b", PINK),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_vertex(animated_graph[("b")], PINK),
            self.color_vertex_label(animated_graph[("b")], BLACK),
            run_time=vertex_change_run_time
        )
        # Step 5. Travel to node e
        network_x_graph.nodes["e"]["cost"] = 17
        self.play(
            self.color_edge(animated_graph.edges[("b", "e")], YELLOW),
            self.change_cell_text(cost_cell_array[4], "17", YELLOW),
            self.change_cell_text(node_cell_array[4], "e", YELLOW),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], GREEN),
            self.color_edge(animated_graph.edges[("b", "c")], GREEN),
            self.change_cell_text(cost_cell_array[1], "13", GREEN),
            self.change_cell_text(node_cell_array[1], "b", GREEN),
            self.color_vertex(animated_graph[("b")], GREEN),
            self.color_vertex_label(animated_graph[("b")], BLACK),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], PINK),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("b", "c")], PINK),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("b", "e")], PINK),
            self.change_cell_text(cost_cell_array[4], "17", PINK),
            self.change_cell_text(node_cell_array[4], "e", PINK),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_vertex(animated_graph[("e")], PINK),
            self.color_vertex_label(animated_graph[("e")], BLACK),
            run_time=vertex_change_run_time
        )
        # Step 6. Travel to node f
        network_x_graph.nodes["f"]["cost"] = 22
        self.play(
            self.color_edge(animated_graph.edges[("e", "f")], YELLOW),
            self.change_cell_text(cost_cell_array[5], "22", YELLOW),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], GREEN),
            self.color_edge(animated_graph.edges[("b", "c")], GREEN),
            self.color_edge(animated_graph.edges[("b", "e")], GREEN),
            self.change_cell_text(cost_cell_array[4], "17", GREEN),
            self.change_cell_text(node_cell_array[4], "e", GREEN),
            self.color_vertex(animated_graph[("e")], GREEN),
            self.color_vertex_label(animated_graph[("e")], BLACK),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], PINK),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("b", "c")], PINK),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("b", "e")], PINK),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("e", "f")], PINK),
            self.change_cell_text(cost_cell_array[5], "22", PINK),
            self.change_cell_text(node_cell_array[5], "f", PINK),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_vertex(animated_graph[("f")], PINK),
            self.color_vertex_label(animated_graph[("f")], BLACK),
            run_time=vertex_change_run_time
        )
        # Step 7. Mark node f as visited
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], GREEN),
            self.color_edge(animated_graph.edges[("b", "c")], GREEN),
            self.color_edge(animated_graph.edges[("b", "e")], GREEN),
            self.color_edge(animated_graph.edges[("e", "f")], GREEN),
            self.change_cell_text(cost_cell_array[5], "22", GREEN),
            self.change_cell_text(node_cell_array[5], "f", GREEN),
            self.color_vertex(animated_graph[("f")], GREEN),
            self.color_vertex_label(animated_graph[("f")], BLACK),
            run_time=edge_change_run_time
        )
        # Step 8. Indicate algorithm completion by marking source node as visited
        self.play(
            self.color_vertex(animated_graph[("a")], GREEN),
            self.color_vertex_label(animated_graph[("a")], BLACK),
            self.change_cell_text(node_cell_array[0], "a", GREEN),
            self.change_cell_text(cost_cell_array[0], "0", GREEN),
            run_time=edge_change_run_time
        )
        # Step 9. Uncolor unvisted edges and wait for 5 seconds
        self.play(
            self.color_edge(animated_graph.edges[("a", "b")], BLUE),
            self.color_edge(animated_graph.edges[("c", "d")], BLUE),
            self.color_edge(animated_graph.edges[("c", "f")], BLUE),
            self.color_edge(animated_graph.edges[("d", "f")], BLUE),
            run_time=edge_change_run_time
        )
        self.wait(5)
        # Step 10. Uncolor all other edges, vertices, and table elements
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], BLUE),
            self.color_edge(animated_graph.edges[("a", "d")], BLUE),
            self.color_edge(animated_graph.edges[("b", "c")], BLUE),
            self.color_edge(animated_graph.edges[("b", "e")], BLUE),
            self.color_edge(animated_graph.edges[("e", "f")], BLUE),
            self.color_vertex(animated_graph[("a")], WHITE),
            self.color_vertex_label(animated_graph[("a")], BLACK),
            self.color_vertex(animated_graph[("b")], WHITE),
            self.color_vertex_label(animated_graph[("b")], BLACK),
            self.color_vertex(animated_graph[("c")], WHITE),
            self.color_vertex_label(animated_graph[("c")], BLACK),
            self.color_vertex(animated_graph[("d")], WHITE),
            self.color_vertex_label(animated_graph[("d")], BLACK),
            self.color_vertex(animated_graph[("e")], WHITE),
            self.color_vertex_label(animated_graph[("e")], BLACK),
            self.color_vertex(animated_graph[("f")], WHITE),
            self.color_vertex_label(animated_graph[("f")], BLACK),
            self.change_cell_text(node_cell_array[0], "a", WHITE),
            self.change_cell_text(cost_cell_array[0], str(network_x_graph.nodes["a"]["cost"]), WHITE),
            self.change_cell_text(node_cell_array[1], "b", WHITE),
            self.change_cell_text(cost_cell_array[1], str(network_x_graph.nodes["b"]["cost"]), WHITE),
            self.change_cell_text(node_cell_array[2], "c", WHITE),
            self.change_cell_text(cost_cell_array[2], str(network_x_graph.nodes["c"]["cost"]), WHITE),
            self.change_cell_text(node_cell_array[3], "d", WHITE),
            self.change_cell_text(cost_cell_array[3], str(network_x_graph.nodes["d"]["cost"]), WHITE),
            self.change_cell_text(node_cell_array[4], "e", WHITE),
            self.change_cell_text(cost_cell_array[4], str(network_x_graph.nodes["e"]["cost"]), WHITE),
            self.change_cell_text(node_cell_array[5], "f", WHITE),
            self.change_cell_text(cost_cell_array[5], str(network_x_graph.nodes["f"]["cost"]), WHITE),
            run_time=edge_change_run_time
        )
        # Step 11. Highlight each shortest path in the graph
        self.play(
            self.color_vertex(animated_graph[("a")], GREEN),
            self.color_vertex_label(animated_graph[("a")], BLACK),
            self.change_cell_text(node_cell_array[0], "a", GREEN),
            self.change_cell_text(cost_cell_array[0], "0", GREEN),
            run_time=edge_change_run_time
        )
        self.wait(3)
        self.play(
            self.color_vertex(animated_graph[("a")], WHITE),
            self.color_vertex_label(animated_graph[("a")], BLACK),
            self.change_cell_text(node_cell_array[0], "a", WHITE),
            self.change_cell_text(cost_cell_array[0], "0", WHITE),
            run_time=edge_change_run_time
        )
        self.wait(3)
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], GREEN),
            self.color_edge(animated_graph.edges[("b", "c")], GREEN),
            self.change_cell_text(cost_cell_array[1], "13", GREEN),
            self.change_cell_text(node_cell_array[1], "b", GREEN),
            self.color_vertex(animated_graph[("b")], GREEN),
            self.color_vertex_label(animated_graph[("b")], BLACK),
            run_time=edge_change_run_time
        )
        self.wait(3)
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], BLUE),
            self.color_edge(animated_graph.edges[("b", "c")], BLUE),
            self.change_cell_text(cost_cell_array[1], "13", WHITE),
            self.change_cell_text(node_cell_array[1], "b", WHITE),
            self.color_vertex(animated_graph[("b")], WHITE),
            self.color_vertex_label(animated_graph[("b")], BLACK),
            run_time=edge_change_run_time
        )
        self.wait(3)
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], GREEN),
            self.change_cell_text(cost_cell_array[2], "12", GREEN),
            self.change_cell_text(node_cell_array[2], "c", GREEN),
            self.color_vertex(animated_graph[("c")], GREEN),
            self.color_vertex_label(animated_graph[("c")], BLACK),
            run_time=edge_change_run_time
        )
        self.wait(3)
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], BLUE),
            self.change_cell_text(cost_cell_array[2], "12", WHITE),
            self.change_cell_text(node_cell_array[2], "c", WHITE),
            self.color_vertex(animated_graph[("c")], WHITE),
            self.color_vertex_label(animated_graph[("c")], BLACK),
            run_time=edge_change_run_time
        )
        self.wait(3)
        self.play(
            self.color_edge(animated_graph.edges[("a", "d")], GREEN),
            self.change_cell_text(cost_cell_array[3], "8", GREEN),
            self.change_cell_text(node_cell_array[3], "d", GREEN),
            self.color_vertex(animated_graph[("d")], GREEN),
            self.color_vertex_label(animated_graph[("d")], BLACK),
            run_time=edge_change_run_time
        )
        self.wait(3)
        self.play(
            self.color_edge(animated_graph.edges[("a", "d")], BLUE),
            self.change_cell_text(cost_cell_array[3], "8", WHITE),
            self.change_cell_text(node_cell_array[3], "d", WHITE),
            self.color_vertex(animated_graph[("d")], WHITE),
            self.color_vertex_label(animated_graph[("d")], BLACK),
            run_time=edge_change_run_time
        )
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], GREEN),
            self.color_edge(animated_graph.edges[("b", "c")], GREEN),
            self.color_edge(animated_graph.edges[("b", "e")], GREEN),
            self.change_cell_text(cost_cell_array[4], "17", GREEN),
            self.change_cell_text(node_cell_array[4], "e", GREEN),
            self.color_vertex(animated_graph[("e")], GREEN),
            self.color_vertex_label(animated_graph[("e")], BLACK),
            run_time=edge_change_run_time
        )
        self.wait(3)
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], BLUE),
            self.color_edge(animated_graph.edges[("b", "c")], BLUE),
            self.color_edge(animated_graph.edges[("b", "e")], BLUE),
            self.change_cell_text(cost_cell_array[4], "17", WHITE),
            self.change_cell_text(node_cell_array[4], "e", WHITE),
            self.color_vertex(animated_graph[("e")], WHITE),
            self.color_vertex_label(animated_graph[("e")], BLACK),
            run_time=edge_change_run_time
        )
        self.wait(3)
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], GREEN),
            self.color_edge(animated_graph.edges[("b", "c")], GREEN),
            self.color_edge(animated_graph.edges[("b", "e")], GREEN),
            self.color_edge(animated_graph.edges[("e", "f")], GREEN),
            self.change_cell_text(cost_cell_array[5], "22", GREEN),
            self.change_cell_text(node_cell_array[5], "f", GREEN),
            self.color_vertex(animated_graph[("f")], GREEN),
            self.color_vertex_label(animated_graph[("f")], BLACK),
            run_time=edge_change_run_time
        )
        self.wait(3)
        self.play(
            self.color_edge(animated_graph.edges[("a", "c")], BLUE),
            self.color_edge(animated_graph.edges[("b", "c")], BLUE),
            self.color_edge(animated_graph.edges[("b", "e")], BLUE),
            self.color_edge(animated_graph.edges[("e", "f")], BLUE),
            self.change_cell_text(cost_cell_array[5], "22", WHITE),
            self.change_cell_text(node_cell_array[5], "f", WHITE),
            self.color_vertex(animated_graph[("f")], WHITE),
            self.color_vertex_label(animated_graph[("f")], BLACK),
            run_time=edge_change_run_time
        )
        self.wait(3)
        self.wait(5)

    # CUSTOM ANIMATION FUNCTIONS
    # Function that colors the fill of a vertex
    def color_vertex(self, vertex, color):
        return vertex[0].animate.set_color(color)

    # Function that colors the label of a vertex
    def color_vertex_label(self, vertex, color):
        return vertex[1].animate.set_color(color)

    # Function that colors an edge in a graph
    def color_edge(self, edge, color):
        return edge.animate.set_color(color)

    # Function that changes the text of a cell in a table
    def change_cell_text(self, cell, text, color):
        return Transform(cell, Text(text).scale(0.7).move_to(cell).set_color(color))
