import networkx as nx
import matplotlib.pyplot as plt

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskals_algorithm(graph, num_vertices):
    result = []
    i = 0
    e = 0
    graph = sorted(graph, key=lambda item: item[2])
    parent = []
    rank = []
    for node in range(num_vertices):
        parent.append(node)
        rank.append(0)
    while e < num_vertices - 1:
        u, v, weight = graph[i]
        i += 1
        x = find(parent, u - 1)
        y = find(parent, v - 1)
        if x != y:
            e += 1
            result.append((u, v, weight))
            union(parent, rank, x, y)
    return result

def display_graph(graph, mst_edges):
    G = nx.Graph()
    for u, v, weight in graph:
        G.add_edge(u, v, weight=weight)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=12, font_color='black', font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    mst_graph = nx.Graph()
    mst_graph.add_weighted_edges_from(mst_edges)
    nx.draw(mst_graph, pos, edge_color='red', width=2, with_labels=True)
    plt.title("Minimum Spanning Tree")
    plt.show()

if __name__ == "__main__":
    num_vertices = int(input("Enter the number of vertices: "))
    graph = []
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, weight = map(int, input("Enter edge (u, v) and weight (space-separated): ").split())
        graph.append((u, v, weight))
    mst = kruskals_algorithm(graph, num_vertices)
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} - {v}: {weight}")
    display_graph(graph, mst)
