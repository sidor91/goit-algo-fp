import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="lightgray"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_heap_tree(heap, index=0):
    """Рекурсивно будує дерево з масиву купи"""
    if index >= len(heap):
        return None

    node = Node(heap[index])
    node.left = build_heap_tree(heap, 2 * index + 1)
    node.right = build_heap_tree(heap, 2 * index + 2)
    return node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [tree.nodes[node]['color'] for node in tree.nodes]
    labels = {node: tree.nodes[node]['label'] for node in tree.nodes}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2000, node_color=colors)
    plt.title(title)
    plt.show()


def generate_color_gradient(start_hex, end_hex, steps):
    """Генерує градієнт з кольорів від start_hex до end_hex"""
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(rgb_color):
        return "#{:02X}{:02X}{:02X}".format(*rgb_color)

    start_rgb = hex_to_rgb(start_hex)
    end_rgb = hex_to_rgb(end_hex)

    gradient = []
    for i in range(steps):
        interpolated = tuple(
            int(start_rgb[j] + (float(i) / (steps - 1)) * (end_rgb[j] - start_rgb[j]))
            for j in range(3)
        )
        gradient.append(rgb_to_hex(interpolated))
    return gradient


def bfs_visualize(root):
    """Обхід у ширину (черга) з візуалізацією"""
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node is None:
            continue
        visited.append(node)
        queue.append(node.left)
        queue.append(node.right)

    colors = generate_color_gradient("#003366", "#99CCFF", len(visited))
    for i, node in enumerate(visited):
        node.color = colors[i]

    draw_tree(root, "Обхід у ширину (BFS)")


def dfs_visualize(root):
    """Обхід у глибину (стек) з візуалізацією"""
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node is None or node in visited:
            continue
        visited.append(node)
        stack.append(node.right)  # спочатку правий, щоб лівий оброблявся першим
        stack.append(node.left)

    colors = generate_color_gradient("#660000", "#FF9999", len(visited))
    for i, node in enumerate(visited):
        node.color = colors[i]

    draw_tree(root, "Обхід у глибину (DFS)")


# Тестування з прикладом купи
heap = [10, 15, 30, 40, 50, 100, 40]
tree_root = build_heap_tree(heap)

# DFS
dfs_visualize(tree_root)

# BFS
tree_root_bfs = build_heap_tree(heap)
bfs_visualize(tree_root_bfs)