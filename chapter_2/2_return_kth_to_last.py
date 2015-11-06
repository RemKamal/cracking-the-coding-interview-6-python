import unittest
from linked_list import *

# time: O(n) space: in-place
def return_k(linked_list, k):
	node = linked_list.head
	for i in range(len(linked_list) - k):
		if node is not None:
			node = node.next
		else:
			return
	return node

class Test(unittest.TestCase):

	def test(self):
		ll1 = random_list(5, 1)
		node1 = Node(2)
		node1.next = Node(9)
		ll2 = random_list(20, 42)
		node2 = Node(26)
		node2.next = Node(0)

		self.failUnlessEqual(return_k(ll1, 5), node1)
		self.failUnlessEqual(return_k(ll2, 2), node2)

if __name__ == "__main__":
	unittest.main()