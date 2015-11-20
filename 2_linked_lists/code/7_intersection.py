import unittest
from linked_list import *

# time: O(n) space: in-place
# the question needs more clarification
def intersection(L1, L2):
	shorter, longer = (L2, L1) if len(L1) > len(L2) else (L1, L2)
	node1, node2 = longer.head, shorter.head
	gap = len(longer) - len(shorter)
	step = 0
	while node1 is not None and node2 is not None:
		while step < gap:
			step += 1
			node1 = node1.next

		if node1 == node2:
			return node1
		else:
			node1, node2 = node1.next, node2.next

class Test(unittest.TestCase):

	def test(self):
		ll1 = LinkedList()
		ll2 = LinkedList()

		for i in [0, 1, 2, 3, 4, 5]:
			ll1.insert(i)
		for i in [0, 1, 2, 5, 8, 9, 10]:
			ll2.insert(i)

		node = Node(2)
		node.set_next(Node(1))

		self.failUnlessEqual(intersection(ll1, ll2), node)

if __name__ == '__main__':
	unittest.main()