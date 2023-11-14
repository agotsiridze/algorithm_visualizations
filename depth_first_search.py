import queue

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


vertices_qty = 20
chance_to_connect = 0.2
frame_time = 0.5


random_matrix = (
    np.random.rand(vertices_qty, vertices_qty) < chance_to_connect / 2
).astype(np.uint8)

np.fill_diagonal(random_matrix, 0, wrap=False)

G = nx.from_numpy_array(random_matrix)


def order_bfs(graph, start_node, end_node):
    visited = set()
    q = queue.Queue()
    q.put(start_node)
    order = []

    nx.draw_kamada_kawai(
        graph,
        with_labels=True,
        edge_color=["b" for _ in graph.edges()],
        node_color=["g" if n == start_node else "olive" for n in graph.nodes],
        alpha=0.9,
    )
    plt.pause(frame_time)

    while not q.empty():
        vortex = q.get()

        if vortex not in visited:
            order.append(vortex)
            visited.add(vortex)

            colors = []
            for node in graph.nodes():
                if node == start_node:
                    colors.append("lime")
                elif node in visited:
                    colors.append("cyan")
                elif node == end_node:
                    colors.append("violet")
                else:
                    colors.append("olive")

            plt.clf()
            nx.draw_kamada_kawai(
                graph,
                with_labels=True,
                edge_color=["b" for _ in graph.edges()],
                node_color=colors,
                alpha=0.9,
            )
            plt.pause(frame_time)

            for node in graph[vortex]:
                if node not in visited:
                    q.put(node)

            if vortex == end_node:
                colors = []
                for node in graph.nodes():
                    if node == start_node or node == end_node:
                        colors.append("lime")
                    elif node in visited:
                        colors.append("cyan")
                    else:
                        colors.append("olive")

                plt.clf()
                nx.draw_kamada_kawai(
                    graph,
                    with_labels=True,
                    edge_color=["b" for _ in graph.edges()],
                    node_color=colors,
                    alpha=0.9,
                )
                plt.show()
                break


order_bfs(G, 0, vertices_qty - 1)
