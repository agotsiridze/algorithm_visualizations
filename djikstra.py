import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import heapq

vertices_qty = 20
chance_to_connect = 0.1
max_weight = 10

frame_time = 0.5


# create weighted directional graph
adjacency_matrix = (
    np.random.rand(vertices_qty, vertices_qty) < chance_to_connect
).astype("bool")
random_weights = np.random.rand(vertices_qty, vertices_qty).round(1)
adjacency_matrix = adjacency_matrix * random_weights
np.fill_diagonal(adjacency_matrix, 0, wrap=False)
# print(adjacency_matrix)
G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)


# visualize
layout = nx.shell_layout(G)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw(G, layout)
nx.draw_networkx_edge_labels(
    G,
    pos=layout,
    edge_labels=edge_labels,
    font_size=6,
    # bbox={"fill ": False},
    clip_on=False,
)

dict_graph = dict()

for k, v in edge_labels.items():
    if k[0] in dict_graph:
        dict_graph[k[0]].append((k[1], v))
    else:
        dict_graph[k[0]] = [(k[1], v)]


plt.show()


def lazy_dijkstras(graph, root):
    dist = [np.Inf for _ in range(vertices_qty)]
    dist[root] = 0
    visited = [False for _ in range(vertices_qty)]
    pq = [(0, root)]
    while len(pq) > 0:
        _, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        if u not in graph:
            continue
        for v, l in graph[u]:
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
                heapq.heappush(pq, (dist[v], v))
    return dist


print(dict_graph)

print(lazy_dijkstras(dict_graph, 0))
