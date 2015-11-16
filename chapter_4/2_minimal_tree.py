import unittest

class TreeNode():

	def __init__(self, item, left = None, right = None, parent = None):
		self.value = item
		self.left = left
		self.right = right
		self.parent = parent

	def inorder(self, orders):
		if self:
			if self.left:
				self.left.inorder(orders)
			orders.append(self.value)
			if self.right:
				self.right.inorder(orders)
		

class BST():

	def __init__(self):
		self.root = None

	# Time: O(lgN) Space: O(N)
	def insert_array(self, array):
		if len(array) == 0: return
		if len(array) == 1: return TreeNode(array[0])

		mid = len(array) / 2
		self.root = TreeNode(array[mid], left = self.insert_array(array[:mid]), right = self.insert_array(array[mid+1:]))
		return self.root

	def inorder(self):
		if self.root:
			orders = []
			self.root.inorder(orders)
			return orders

class Test(unittest.TestCase):

	def test(self):
		array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		tree = BST()
		tree.insert_array(array)

		self.failUnlessEqual(tree.inorder(), array)

if __name__ == '__main__':
	unittest.main()