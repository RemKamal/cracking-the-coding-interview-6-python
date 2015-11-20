import unittest
from collections import deque

# Time: O(E) Space: O(V)
def bfs(G, v1, v2):
	visited = {v1: 0}
	queue = deque()
	queue.append(v1)
	while queue:
		v = queue.pop()
		for nb in G[v]:
			if nb not in visited:
				visited[nb] = visited[v] + 1
				queue.append(nb)

	if v2 in visited:
		return True
	else:
		return False

class Test():

	def test(self):
		G = {'a': ['b', 'c'],
			 'b': ['a', 'c', 'd'],
			 'c': ['a', 'b'],
			 'd': ['b'],
			 'e':[]}

		self.assertTrue(bfs(G, 'a', 'd'))
		self.assertFalse(bfs(G, 'a', 'e'))

if __name__ == '__main__':
	unittest.main()