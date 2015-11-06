import unittest
from linked_list import *

# time: O(n) space: in-place
def remove_middle(linked_list, item):
	node = linked_list.head
	pre = None
	while node is not None:
		if node.value == item:
			pre.next = node.next
			return
		else:
			pre = node
			node = node.next
	if node is None:
		pre = None
	raise KeyError("item not in the list!")

class Test(unittest.TestCase):

	def test(self):
		ll1 = random_list(5, 1)
		ll2 = random_list(10, 1)
		self.failUnlessEqual(remove_middle(ll1, 2), ll1.remove(2))
		self.failUnlessEqual(remove_middle(ll2, 5), ll2.remove(5))


if __name__ == "__main__":
	unittest.main()