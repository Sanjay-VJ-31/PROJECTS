import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def floyd(n, cost_matrix):
    distances = np.array(cost_matrix, copy=True)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][k] != np.inf and distances[k][j] != np.inf:
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances
def print_all_pairs_shortest_paths(distances):
    print("\nAll-pairs shortest paths matrix:")
    n = len(distances)
    for i in range(n):
        for j in range(n):
            if distances[i][j] == np.inf:
                print("inf", end="\t")
            else:
                print(f"{distances[i][j]:.0f}", end="\t")
        print()
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
    plt.title("Graph Representation with Weights")
    plt.show()

n = int(input("Enter the number of nodes: "))
cost_matrix = np.full((n, n), np.inf)
print("\nEnter the cost for each pair of nodes:")
print("Use 'inf' for no connection.\n")
for i in range(n):
    for j in range(n):
        if i == j:
            cost_matrix[i][j] = 0  # Distance to self is always 0
            continue
        value = input(f"Enter the Distance from vertex {i} to vertex {j} (enter 'inf' if no connection): ")
        cost_matrix[i][j] = np.inf if value.lower() in ["inf","i", "infinity"] else float(value)
distances = floyd(n, cost_matrix)
print_all_pairs_shortest_paths(distances)
visualize_graph(n, cost_matrix)
