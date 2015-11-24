from collections import deque

class Node(object):

    def __init__(self, item):
        self.value = item
        self.next = None

class LinkedList(object):

    def __init__(self):
        self.head = None

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def __str__(self):
        node = self.head
        result = ""
        while node is not None:
            item = node.value
            node = node.next
            if node is None:
                linked = None
            else:
                linked = node.value
            result += str(item) + " -> " + str(linked) + "\n"
        return result


class TreeNode(object):
    def __init__(self, item):
        self.value = item
        self.parent = None
        self.left = None
        self.right = None

def tree_from_array(array):
    if array == []: return
    mid = len(array) / 2
    node = TreeNode(array[mid])
    node.left = tree_from_array(array[:mid])
    node.right = tree_from_array(array[mid + 1:])
    return node

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

if __name__ == '__main__':
    main()