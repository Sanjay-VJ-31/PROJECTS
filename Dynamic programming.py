import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def dynamicprogramming(n, cost_matrix, destination):
    distances = np.full(n, np.inf)
    distances[destination] = 0
    previous = [None] * n

    for i in range(n - 1, -1, -1):
        for j in range(n):
            if cost_matrix[j][i] != np.inf:
                new_distance = distances[i] + cost_matrix[j][i]
                if new_distance < distances[j]:
                    distances[j] = new_distance
                    previous[j] = i

    return distances, previous
def print_single_destination_paths(destination, distances, previous):
    print(f"\nDistances to destination {destination}:")
    for source, dist in enumerate(distances):
        if dist == np.inf:
            print(f"Node {source}: No path")
        else:
            path = []
            current = source
            while current is not None:
                path.append(current)
                current = previous[current]
            print(f"Node {source}: Path {' -> '.join(map(str, reversed(path)))} with distance {dist}")
def visualize_graph(n, cost_matrix):
    G = nx.DiGraph()
    for i in range(n):
        for j in range(n):
            if cost_matrix[i][j] != np.inf:
                G.add_edge(i, j, weight=cost_matrix[i][j])

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()
n = int(input("Enter the number of nodes: "))
cost_matrix = np.full((n, n), np.inf)
for i in range(n):
    for j in range(n):
        value = input(f"Enter the Distance from vertex {i} to vertex {j} (enter 'inf' if no connection): ")
        cost_matrix[i][j] = np.inf if value.lower() in ["inf","i", "infinity"] else float(value)
destination = int(input("Enter the destination node (0-indexed): "))
distances, previous = dynamicprogramming(n, cost_matrix, destination)
print_single_destination_paths(destination, distances, previous)
visualize_graph(n, cost_matrix)
