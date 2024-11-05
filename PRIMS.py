import networkx as nx
import matplotlib.pyplot as plt

def prims_algorithm(graph, start_vertex):
    mst_edges = []
    total_cost = 0
    visited = set()
    visited.add(start_vertex)
    while len(visited) < len(graph):
        min_edge = (None, None, float('inf'))
        for u in visited:
            for v, weight in graph[u]:
                if v not in visited and weight < min_edge[2]:
                    min_edge = (u, v, weight)
        if min_edge[0] is not None:
            mst_edges.append((min_edge[0], min_edge[1], min_edge[2]))
            total_cost += min_edge[2]
            visited.add(min_edge[1])
    return mst_edges, total_cost

def display_graph(graph, mst_edges):
    G = nx.Graph()
    for u in graph:
        for v, weight in graph[u]:
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
    graph = {i: [] for i in range(1, num_vertices + 1)}

    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, weight = map(int, input("Enter edge (u, v) and weight (space-separated): ").split())
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    start_vertex = int(input("Enter the starting vertex: "))
    mst, cost = prims_algorithm(graph, start_vertex)
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} - {v}: {weight}")
    print(f"Total cost of the Minimum Spanning Tree: {cost}")
    display_graph(graph, mst)


