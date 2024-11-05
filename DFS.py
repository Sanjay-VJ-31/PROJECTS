import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, node, visited=None, traversal=None, pos=None):
    G = nx.DiGraph(graph)
    if visited is None:
        visited = set()
    if traversal is None:
        traversal = []
    pos = nx.spring_layout(G)  
    visited.add(node)
    traversal.append(node)
    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color=["yellow" if n in visited else "lightblue" for n in G.nodes])
    plt.title(f"DFS Visited: {node}")
    plt.pause(1)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal, pos)
    return traversal

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
        print(f"Visualizing DFS starting from node '{start_node}'...")
        dfs_result = dfs(graph, start_node)
    plt.show()
