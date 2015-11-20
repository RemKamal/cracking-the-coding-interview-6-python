import unittest

# Time: O(n) Space: O(n)
def memo(func):
	cache = {}
	def wrapper(n):
		if n not in cache:
			cache[n] = func(n)
		return cache[n]
	return wrapper

@memo
def triple_step(n):
	if n < 0:
		return 0
	if n == 0:
		return 1
	return triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)

class Test(unittest.TestCase):

	def test(self):
		self.failUnlessEqual(triple_step(1), 1)
		self.failUnlessEqual(triple_step(2), 2)
		self.failUnlessEqual(triple_step(3), 4)
		self.failUnlessEqual(triple_step(30), 53798080)

if __name__ == '__main__':
	unittest.main()