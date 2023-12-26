import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import heapq


class GraphVisualizer:
    def __init__(self, vertices_qty: int) -> None:
        """Create graph and visualize

        args:
            vertices_qty: int - number of vertices in graph

        """
        self.vertices_qty = vertices_qty
        self._graph = None
        self.layout = None
        self.edge_labels = None
        self.edges = None
        self.colors = None
        self.weight_baldness = None
        self.vertices_colors = None

    @property
    def graph(self) -> nx.classes.digraph.DiGraph:
        return self._graph

    @graph.setter
    def graph(self, adjacency_matrix: np.array) -> None:
        """Creates graph and elements for visualization using Networkx library.

        args:
            adjacency_matrix: np.array - matrix to represent connections between nodes

        """
        self._graph = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)
        self.layout = nx.circular_layout(self._graph)

        self.edge_labels = nx.get_edge_attributes(self._graph, "weight")
        self.edges = self._graph.edges()
        self.colors = ["aquamarine" for _ in self.edges]
        self.weight_baldness = [v * 3 for _, v in self.edge_labels.items()]

    def __dict__(self):
        dict_graph = dict()
        for k, v in self.edge_labels.items():
            if k[0] in dict_graph:
                dict_graph[k[0]].append((k[1], v))
            else:
                dict_graph[k[0]] = [(k[1], v)]
        return dict_graph

    def lazy_dijkstras(self, root, visualize=True):
        """Calculates distances from starting node to every possible node and visualizes it

        root: int - index of starting node
        visualize: bool - if true create popup for visualization
        """
        distances = [np.Inf for _ in range(self.vertices_qty)]
        distances[root] = 0
        visited = [False for _ in range(self.vertices_qty)]
        pq = [(0, root)]

        if visualize:
            fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
        while len(pq) > 0:
            _, u = heapq.heappop(pq)

            if visited[u]:
                continue
            if u not in self.__dict__():
                continue
            visited[u] = True
            for next_node, weight in self.__dict__()[u]:
                if visualize:
                    edge_index = list(self.edges).index((u, next_node))
                    self.colors[edge_index] = "orangered"
                    self.show_subplots(axes[0], axes[1], distances, visited)
                    self.colors[edge_index] = "tomato"

                if distances[u] + weight < distances[next_node]:
                    distances[next_node] = distances[u] + weight
                    heapq.heappush(pq, (distances[next_node], next_node))
                    if visualize:
                        self.colors[edge_index] = "lime"
                        self.show_subplots(axes[0], axes[1], distances, visited)

        return distances

    def show_subplots(self, ax1, ax2, distances, visited):
        ax1.clear()
        ax2.clear()
        # bar visualization
        col_colors = []
        for dist in distances:
            if dist < 0.5:
                col_colors.append("springgreen")
            elif dist < 1.3:
                col_colors.append("sandybrown")
            else:
                col_colors.append("orangered")
        ax1.bar([i for i in range(len(distances))], distances, color=col_colors)
        ax1.get_xaxis().set_major_locator(plt.MaxNLocator(integer=True))
        ax1.set_xticks(range(len(distances)))
        ax1.set_xticklabels(range(len(distances)))

        # graph visualizations
        color_map = ["limegreen" if color else "cornflowerblue" for color in visited]
        nx.draw(
            self._graph,
            self.layout,
            edge_color=self.colors,
            width=self.weight_baldness,
            node_color=color_map,
        )
        nx.draw_networkx_labels(self._graph, self.layout, font_size=10)
        nx.draw_networkx_edge_labels(
            self._graph,
            pos=self.layout,
            edge_labels=self.edge_labels,
            font_size=6,
            clip_on=False,
        )
        plt.pause(0.5)


if __name__ == "__main__":
    # define constants
    VERTICES_QTY = 20
    chance_to_connect = 0.1
    FRAME_TIME = 0.0001

    # create random adjacency matrix
    adjacency_matrix = (
        np.random.rand(VERTICES_QTY, VERTICES_QTY) < chance_to_connect
    ).astype("bool")
    random_weights = np.random.rand(VERTICES_QTY, VERTICES_QTY).round(1)
    adjacency_matrix = adjacency_matrix * random_weights
    np.fill_diagonal(adjacency_matrix, 0, wrap=False)

    # create Graph
    G = GraphVisualizer(VERTICES_QTY)
    G.graph = adjacency_matrix

    # run algorithm with visualizations
    G.lazy_dijkstras(0, True)
    plt.show()
