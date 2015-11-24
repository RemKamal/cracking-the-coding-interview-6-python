from collections import deque

def get_level(node):
    queue = deque()
    prev = 0
    queue.append((node, prev))
    visited, graph, level = [node], [], []

    while queue:
        node, height = queue.popleft()
        if height != prev:
            prev = height
            graph.append(level)
            level = [node.value]
        else:
            level.append(node.value)

        if node.left and node.left not in visited:
            visited.append(node.left)
            queue.append((node.left, height + 1))
        if node.right and node.right not in visited:
            visited.append(node.right)
            queue.append((node.right, height + 1))

    graph.append(level)

    return graph