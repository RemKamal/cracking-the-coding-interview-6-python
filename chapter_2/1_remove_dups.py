import unittest
from linked_list import *

# time: O(n) space: O(n)
def remove_dups(linked_list):
    node = linked_list.head
    tracer = [node.value]
    pre = None
    while node is not None:
        pre = node
        node = node.next
        if node is not None:
            if node.value in tracer:
                pre.next = node.next
                node = pre
            else:
                tracer.append(node.value)
    return linked_list

class Test(unittest.TestCase):

    def unique_items(self, linked_list):
        items = set()
        for i in linked_list:
            items.add(i)
        return len(items)

    def test(self):
        ll1 = random_list(5, 1)
        ll2 = random_list(100, 42)

        self.failUnlessEqual(len(remove_dups(ll1)), self.unique_items(ll1))
        self.failUnlessEqual(len(remove_dups(ll2)), self.unique_items(ll2))

if __name__ == "__main__":
    unittest.main()