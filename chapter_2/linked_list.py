import random

class LinkedList():
    """Helper function to create a linked list in Python"""
    def __init__(self):
        self.head = None

    def insert(self, item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node

    def size(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def __len__(self):
        return self.size()

    def search(self, item):
        node = self.head
        found = False
        while node is not None and not found:
            if node.value == item:
                found = True
            else:
                node = node.next
        return found

    def __contains__(self, item):
        return self.search(item)

    def remove(self, item):
        node = self.head
        found = False
        previous = None
        while not found and node is not None:
            if node.value == item:
                found = True
            else:
                previous = node
                node = node.next

        if node is None: raise KeyError("item not in the list!")
        if previous is None:
            self.head = node.next
        else:
            previous.set_next(node.next)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.value
            node = node.next

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

    def __eq__(self, new_linked_list):
        node1, node2 = self.head, new_linked_list.head
        while node1 is not None and node2 is not None:
            if node1.value != node2.value:
                return False
            node1, node2 = node1.next, node2.next
        return True
        
class Node():
    """Node object in LinkedList"""
    def __init__(self, item):
        self.value = item
        self.next = None

    def set_item(self, item):
        self.value = item

    def set_next(self, next):
        self.next = next

    def __str__(self):
        return str((self.value, self.next))

    def __eq__(self, new_node):
        if self.next is None:
            return self.value == new_node.value and new_node.next is None
        elif new_node.next is not None:
            return self.value == new_node.value and self.next.value == new_node.next.value
        else:
            return False

def random_list(n, random_state=42):
    ll = LinkedList()
    random.seed(random_state)
    randoms = [random.randint(0, n * 2) for i in range(n)]
    for i in range(n):
        ll.insert(i)
        ll.insert(randoms[i])
    return ll