import unittest

class Grid():
	def __init__(self, r, c):
		self.r = r
		self.c = c
		self.destination = (r - 1, c - 1)
		self.blocked = []

	def add_block(self, r, c):
		if self.is_legal(r, c):
			self.blocked.append((r, c))

	def is_legal(self, r, c):
		return (0 <= r < self.r and
			    0 <= c < self.c and
			    (r, c) not in self.blocked)

	def __str__(self):
		grid = [[1 for c in range(self.c)] for r in range(self.r)]
		for node in self.blocked:
			r, c = node
			grid[r][c] = 0
		return str(grid)

	def find_path(self, r = 0, c = 0):
		# use a DFS
		stack = [(r, c)]
		visited = []
		path = []

		while stack:
			node = stack.pop()
			r, c = node
			if node not in visited:
				visited.append(node)
				if node == self.destination:
					path.append(node)
					return path

				neighbors = [(r, c + 1), (r + 1, c)] # Go right fisrt
				valid_path = 0
				for nb in neighbors:
					if self.is_legal(*nb):
						stack.append(nb)
						valid_path += 1

				if valid_path == 0:
					path.pop()
				else:
					path.append(node)
				
		return "not found"

class Test(unittest.TestCase):

	def test(self):

		g1 = Grid(3, 3)
		for node in [(0, 1), (1, 2), (2, 0)]:
			g1.add_block(*node)

		g2 = Grid(5, 5)
		for node in [(0, 1), (2, 0), (2, 1), (4, 2), (1, 3), (2, 3), (3, 4)]:
			g2.add_block(*node)

		expected1 = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]
		expected2 = [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4)]

		self.failUnlessEqual(g1.find_path(), expected1)
		self.failUnlessEqual(g2.find_path(), expected2)

if __name__ == '__main__':
	unittest.main()