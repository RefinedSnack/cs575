from typing import Dict, Union, List

import networkx as nx
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import os
import statistics
import numpy as np


def calculate_metrics(graph: nx.Graph) -> Dict[str, Union[int, float, dict]]:
    result = {
        "Number of Vertices": calculate_number_of_vertices(graph),
        "Number of Edges": calculate_number_of_edges(graph),
        "Average Degree": calculate_average_degree(graph),
        "Degree Distribution": calculate_degree_distribution(graph),
        "Median Distance": calculate_median_distance(graph),
        "Median Distance Distribution": calculate_median_distance_distribution(graph),
        "Radius": calculate_radius(graph),
        "Diameter": calculate_diameter(graph),
        "Density": calculate_density(graph),
    }
    return result

def calculate_number_of_vertices(graph: nx.Graph) -> int:
    return len(graph.nodes)

def calculate_number_of_edges(graph: nx.Graph) -> int:
    return len(graph.edges)

def calculate_average_degree(graph: nx.Graph) -> float:
    degrees = [degree for node, degree in graph.degree]
    if len(degrees) > 0:
        return sum(degrees) / len(degrees) 
    else:
        return 0

def calculate_degree_distribution(graph: nx.Graph) -> dict:
    degree_list = [degree for node,degree in graph.degree]
    degree_count = Counter(degree_list)
    return dict(degree_count)

def calculate_median_distance(graph: nx.Graph) -> list:
    median_distance: list = []
    for node in graph.nodes:
        shortest_path_lengths = nx.single_source_shortest_path_length(graph, node)
        distances = list(shortest_path_lengths.values())
        median_distance_val = statistics.median(distances)
        median_distance.append((node, median_distance_val))
    return median_distance
        


def calculate_median_distance_distribution(graph: nx.Graph) -> dict:
    median_distance: list = [y for x,y in calculate_median_distance(graph)]
    return dict(Counter(median_distance))

def calculate_radius(graph: nx.Graph) -> float:
    return nx.radius(graph)

def calculate_diameter(graph: nx.Graph) -> float:
    return nx.diameter(graph)

def calculate_density(graph: nx.Graph) -> float:
    return nx.density(graph)

def create_and_save_distribution(count: dict, output_path: str, metric_name: str) -> None:
    fig, ax = plt.subplots()
    max_val = max(count.keys())
    
    # Check if there are any floats in the keys
    has_floats = any(isinstance(x, float) for x in count.keys())
    xs = [] 
    if has_floats:
        # If there are floats, set the x-axis steps to 0.5
        xs = np.arange(0.0, max_val + 0.5, 0.5)
    else:
        # If there are only ints, set the x-axis steps to 1
        xs = [str(x) for x in range(max_val + 1)]

    
    ys = [count[x] if x in count else 0 for x in xs]
    xs = [str(x) for x in xs]
    bars = ax.bar(xs, ys)

    ax.set_ylabel('Frequency')
    ax.set_xlabel('Value')
    plt.title(f"{metric_name}")

    ax.bar_label(bars, padding=3)

    plt.savefig(output_path)
    plt.close()


def save_graph_as_png(graph: nx.Graph, directory_name: str) -> str:
    # Create the directory if it doesn't exist
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    # Save the graph as a PNG file
    file_path: str = os.path.join(directory_name, 'graph.png')
    nx.draw(graph, with_labels=True)
    plt.savefig(file_path)
    plt.close()  # Close the figure to release resources

    return file_path

def prepare_document(metrics_pairs: Dict[str, Union[int, float, dict, list]], graph_name: str, G: nx.Graph) -> None:
    document = []
    first_graph_path = save_graph_as_png(G, graph_name)
    document.append(f"## {graph_name}\n\n![Graph]({first_graph_path})\n\n")

    for metric_name, metric_value in metrics_pairs.items():
        if isinstance(metric_value, dict):  # Check if the metric is a distribution
            output_path = f"{graph_name}/{metric_name.lower().replace(' ', '_')}_distribution.png"
            create_and_save_distribution(metric_value, output_path, metric_name)
            document.append(f"{metric_name}:\n\n![{metric_name} Distribution]({output_path})\n\n")
        elif isinstance(metric_value, list):
            table_header = f"| Node Index | {metric_name} |\n|------------|------------|\n"
            table_rows = "\n".join(f"| {x} | {val} |" for x, val in metric_value)
            table = f"{table_header}{table_rows}\n\n"
            document.append(table)
        else:
            document.append(f"{metric_name}: {metric_value}\n\n")
    
    with open(graph_name + ".md", "w") as file:
        file.writelines(document)
        
def run(G: nx.Graph, name: str) -> None:
    prepare_document(calculate_metrics(G), name, G)
    
if __name__ == "__main__":
    run(nx.complete_graph(21), "Complete")
    run(nx.barbell_graph(10, 3), "Barbell")
    run(nx.cycle_graph(21), "Cycle")
    run(nx.grid_2d_graph(5, 5), "Lattice")
    run(nx.ladder_graph(21), "Ladder")