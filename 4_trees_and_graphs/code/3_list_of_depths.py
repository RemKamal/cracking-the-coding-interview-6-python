from collections import deque

class TreeNode():

	def __init__(self, item, parent = None):
		self.value = item
		self.parent = parent
		self.left = None
		self.right = None

	def insert(self, node):
		if node is None: return

		if node.value > self.value:
			if self.right:
				self.right.insert(node)
			else:
				self.right = node
		else:
			if self.left:
				self.left.insert(node)
			else:
				self.left = node

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

	def insert(self, item):
		if self.root:
			node = TreeNode(item, parent = self.root)
			self.root.insert(node)
		else:
			self.root = TreeNode(item)

	def inorder(self):
		orders = []
		if self.root:
			self.root.inorder(orders)
		return orders

class Node():

	def __init__(self, item):
		self.value = item
		self.next = None

class LinkedList():

	def __init__(self):
		self.head = None

	def push(self, item):
		node = Node(item)
		node.next = self.head
		self.head = node


	def __str__(self):
		node = self.head
		array = []
		while node:
			array.append(node.value)
			node = node.next
		return str(array)


def convert_to_list(node):
	queue = deque()
	queue.append(node)
	visited = [node.value]
	lists = []
	linked_list = LinkedList()
	node.level = 0

	while queue:
		prev = node
		node = queue.popleft()
		if prev.level < node.level:
			lists.append(linked_list)
			linked_list = LinkedList()
			linked_list.push(node.value)
		else:
			linked_list.push(node.value)

		if node.left:
			if node.left.value not in visited:
				visited.append(node.left.value)
				node.left.level = node.level + 1
				queue.append(node.left)
				
		if node.right:
			if node.right.value not in visited:
				visited.append(node.right.value)
				node.right.level = node.level + 1
				queue.append(node.right)
	lists.append(linked_list)
	return lists

tree = BST()
for i in [6, 4, 8, 1, 5, 7, 9]:
	tree.insert(i)

a = convert_to_list(tree.root)

for i in a:
	print i

print tree.root.value
print tree.root.left.value, tree.root.right.value
print tree.root.left.left.value, tree.root.left.right.value, tree.root.right.left.value, tree.root.right.right.value