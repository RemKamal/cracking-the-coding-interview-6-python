import unittest

class Stack():
	"""
		Space: O(n)
		Push: O(1)
		Pop: O(1)
	"""

	def __init__(self, size = 100, n = 3):
		self.size = size
		self.num = n
		self.array = [None] * (self.size * n)
		self.pointer = [-1] * n

	def push(self, item, num = 0):
		if num > self.num - 1: return "Exceeds number of stacks!"
		if self.pointer[num] >= self.size - 1: return "Stack {} is out of space.".format(num)

		self.pointer[num] += 1
		index = self.size * num + self.pointer[num]
		self.array[index] = item

	def pop(self, num = 0):
		if num > self.num: return "Exceeds number of stacks!"
		if self.pointer[num] < 0: return "Empty stack"
		index = self.size * num + self.pointer[num]
		item = self.array[index]
		self.array[index] = None
		self.pointer[num] -= 1

	def __str__(self):
		result = ""
		for i in range(self.num):
			index = self.size * i
			result += "Stack {}: {}\n".format(i, self.array[index:index + self.size])
		return result

class Test(unittest.TestCase):

	def test(self):
		stack = Stack(size = 10)
		stack.push(1, 0)
		stack.push(10, 1)
		stack.push(4, 1)
		stack.push('a', 2)
		result = [1, None, None, None, None, None, None, None, None, None, 10, 4, None, None, None, None, None, None, None, None, 'a', None, None, None, None, None, None, None, None, None]

		self.failUnlessEqual(stack.array, result)

if __name__ == '__main__':
	unittest.main()

