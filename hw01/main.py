import networkx as nx
import matplotlib.pyplot as plt
import pydot

def add_group(G: nx.Graph, nodes: list):
    for x in nodes:
        for y in nodes:
            if x == y:
                break
            G.add_edge(x, y)

def problem1():
    G = nx.Graph()
    G.add_nodes_from(range(1,15))
    
    
    G.add_edge(7, 6)
    G.add_edge(7, 3)
    G.add_edge(7, 8)
    G.add_edge(8, 12)
    G.add_edge(8, 9)
    add_group(G, [12, 13, 14])
    add_group(G, [4, 5, 6])
    add_group(G, [1, 2, 3])
    add_group(G, [9, 10, 11])
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
    
    
def problem2():
    
    fig = plt.figure(figsize=(15, 15))

    
    complete_graph_10 = nx.complete_graph(10)
    plt.subplot(3, 2, 1)
    nx.draw(complete_graph_10, with_labels=True)
    plt.title("Complete Graph with 10 Vertices")

    
    barbell_graph_10 = nx.barbell_graph(5, 0)
    plt.subplot(3, 2, 2)
    nx.draw(barbell_graph_10, with_labels=True)
    plt.title("Barbell Graph with 10 Vertices")

    
    cycle_graph_10 = nx.cycle_graph(10)
    plt.subplot(3, 2, 3)
    nx.draw(cycle_graph_10, with_labels=True)
    plt.title("Cycle Graph with 10 Vertices")

    
    lattice_graph_10 = nx.grid_2d_graph(3, 4)
    plt.subplot(3, 2, 4)
    nx.draw(lattice_graph_10, with_labels=True)
    plt.title("Lattice (Grid 2D) Graph with 10 Vertices")

    
    ladder_graph_10 = nx.ladder_graph(5)
    plt.subplot(3, 2, 5)
    nx.draw(ladder_graph_10, with_labels=True)
    plt.title("Ladder Graph with 10 Vertices")

    
    complete_graph_20 = nx.complete_graph(20)
    plt.subplot(3, 2, 6)
    nx.draw(complete_graph_20, with_labels=True)
    plt.title("Complete Graph with 20 Vertices")

    
    plt.tight_layout()
    plt.show()

def problem3():
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

    # Set up subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Spring Layout
    pos_spring = nx.spring_layout(G)
    axes[0, 0].set_title('Spring Layout')
    nx.draw(G, pos_spring, with_labels=True, font_weight='bold', node_color='lightblue', edge_color='gray', ax=axes[0, 0])

    # Circular Layout
    pos_circular = nx.circular_layout(G)
    axes[0, 1].set_title('Circular Layout')
    nx.draw(G, pos_circular, with_labels=True, font_weight='bold', node_color='lightcoral', edge_color='gray', ax=axes[0, 1])

    # Graphviz Layout using nx_pydot
    pos_nx_pydot = nx.nx_pydot.graphviz_layout(G, prog="neato")
    axes[1, 0].set_title('Graphviz Layout (nx_pydot)')
    nx.draw(G, pos_nx_pydot, with_labels=True, font_weight='bold', node_color='lightgreen', edge_color='gray', ax=axes[1, 0])

    # Graphviz Layout using a_graph
    pos_a_graph = nx.nx_agraph.graphviz_layout(G, prog="neato")
    axes[1, 1].set_title('Graphviz Layout (a_graph)')
    nx.draw(G, pos_a_graph, with_labels=True, font_weight='bold', node_color='lightcoral', edge_color='gray', ax=axes[1, 1])

    # Adjust layout
    plt.tight_layout()
    plt.show()

def problem4():
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

    # Set up subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Spring Layout
    pos_spring = nx.spring_layout(G)
    axes[0, 0].set_title('Spring Layout')

    # Customize node colors, sizes, and labels
    node_colors_spring = ['lightblue' if node != 3 else 'orange' for node in G.nodes]
    node_sizes_spring = [300 if node != 3 else 600 for node in G.nodes]
    nx.draw(G, pos_spring, with_labels=True, font_weight='bold', node_color=node_colors_spring, node_size=node_sizes_spring, edge_color='gray', ax=axes[0, 0])

    # Circular Layout
    pos_circular = nx.circular_layout(G)
    axes[0, 1].set_title('Circular Layout')

    # Customize node colors, sizes, and labels
    node_colors_circular = ['lightcoral' if node != 2 else 'yellow' for node in G.nodes]
    node_sizes_circular = [300 if node != 2 else 600 for node in G.nodes]
    nx.draw(G, pos_circular, with_labels=True, font_weight='bold', node_color=node_colors_circular, node_size=node_sizes_circular, edge_color='gray', ax=axes[0, 1])

    # Graphviz Layout using nx_pydot
    pos_nx_pydot = nx.nx_pydot.graphviz_layout(G, prog="neato")
    axes[1, 0].set_title('Graphviz Layout (nx_pydot)')

    # Customize node colors, sizes, and labels
    node_colors_nx_pydot = ['lightgreen' if node != 4 else 'red' for node in G.nodes]
    node_sizes_nx_pydot = [300 if node != 4 else 600 for node in G.nodes]
    nx.draw(G, pos_nx_pydot, with_labels=True, font_weight='bold', node_color=node_colors_nx_pydot, node_size=node_sizes_nx_pydot, edge_color='gray', ax=axes[1, 0])

    # Graphviz Layout using a_graph
    pos_a_graph = nx.nx_agraph.graphviz_layout(G, prog="neato")
    axes[1, 1].set_title('Graphviz Layout (a_graph)')

    # Customize node colors, sizes, and labels
    node_colors_a_graph = ['lightcoral' if node != 1 else 'purple' for node in G.nodes]
    node_sizes_a_graph = [300 if node != 1 else 600 for node in G.nodes]
    nx.draw(G, pos_a_graph, with_labels=True, font_weight='bold', node_color=node_colors_a_graph, node_size=node_sizes_a_graph, edge_color='gray', ax=axes[1, 1])

    # Adjust layout
    plt.tight_layout()
    plt.show()


if __name__=="__main__": 
    problem1()
    problem2()
    problem3()
    problem4()