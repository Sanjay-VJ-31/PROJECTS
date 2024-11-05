import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(graph, start_node):
    G = nx.DiGraph(graph)
    pos = nx.spring_layout(G)
    visited = set()
    queue = deque([start_node])
    traversal = []
    plt.figure(figsize=(8, 6))
    step = 0
    while queue:
        node = queue.popleft()
        traversal.append(node)
        visited.add(node)
        plt.clf()
        nx.draw(G, pos, with_labels=True, node_color=["yellow" if n in visited else "lightblue" for n in G.nodes])
        plt.title(f"BFS Step {step}: ")
        plt.pause(1)
        step += 1
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return traversal, visited

def input_graph():
    graph = {}
    print("Enter the graph as 'node: neighbor1, neighbor2':")
    print("Type 'done' when finished.")
    while True:
        line = input("Enter graph: ")
        if line.strip().lower() == 'done':
            break
        try:
            node, neighbors = line.split(':')
            neighbors_list = [n.strip() for n in neighbors.split(',') if n.strip()]  
            graph[node.strip()] = neighbors_list
        except ValueError:
            print("Invalid input format. Please use 'node: neighbor1, neighbor2'.")
    return graph

if __name__ == "__main__":
    graph = input_graph()
    print("Constructed Graph:", graph)
    start_node = input("Enter the starting node: ").strip()
    if start_node not in graph:
        print(f"Error: '{start_node}' is not a valid node in the graph.")
    else:
        print(f"Visualizing BFS starting from node '{start_node}'...")
        bfs_result, visited_all = bfs(graph, start_node)
    plt.show()
