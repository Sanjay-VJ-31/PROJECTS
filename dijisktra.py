import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(n, cost_matrix, source):
    distances = np.full(n, np.inf)
    distances[source] = 0
    previous = [None] * n
    visited = []
    for step in range(n):
        min_distance = np.inf
        next_node = -1
        for i in range(n):
            if i not in visited and distances[i] < min_distance:
                min_distance = distances[i]
                next_node = i
        if next_node == -1:
            break
        visited.append(next_node)
        print(f"\nStep {step + 1}: Processing node {next_node}")
        print("Current distances:", [f"{d:.0f}" if d != np.inf else "∞" for d in distances])
        for destination in range(n):
            if distances[destination] != np.inf:
                path = []
                current = destination
                while current is not None:
                    path.insert(0, current)
                    current = previous[current]
                if path[0] == source:
                    print(f"Path to node {destination}: {' -> '.join(map(str, path))} with distance {distances[destination]}")
        for j in range(n):
            if cost_matrix[next_node][j] != np.inf and j not in visited:
                new_distance = distances[next_node] + cost_matrix[next_node][j]
                if new_distance < distances[j]:
                    distances[j] = new_distance
                    previous[j] = next_node
    print("\nFinal distances and paths from source:")
    for destination in range(n):
        if distances[destination] != np.inf:
            path = []
            current = destination
            while current is not None:
                path.insert(0, current)
                current = previous[current]
            print(f"Path to node {destination}: {' -> '.join(map(str, path))} with distance {distances[destination]}")
def visualize_graph(n, cost_matrix):
    G = nx.DiGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if cost_matrix[i][j] != np.inf:
                G.add_edge(i, j, weight=cost_matrix[i][j])
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title("Graph Representation with Weights")
    plt.show()
n = int(input("Enter the number of nodes: "))
cost_matrix = np.full((n, n), np.inf)
for i in range(n):
    for j in range(n):
        a = input(f"Enter the Distance from vertex {i} to vertex {j} (enter 'inf' if no connection): ")
        if a.lower() in ["inf", "i", "infinity"]:
            cost_matrix[i][j] = np.inf
        else:
            try:
                distance = int(a)
                cost_matrix[i][j] = distance
            except ValueError:
                print("Invalid input. Setting to infinity.")
                cost_matrix[i][j] = np.inf
source = int(input("Enter the source node (0-indexed): "))
dijkstra(n, cost_matrix, source)
visualize_graph(n, cost_matrix)
