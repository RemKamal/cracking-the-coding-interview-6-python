import unittest

class Stack():

	def __init__(self):
		self.size = 0
		self.array = []
		self.min_tracer = []

	def push(self, item):
		self.array.append(item)
		self.size += 1
		if self.size == 1:
			self.min_tracer.append(item)
		else:
			if item < self.min_tracer[-1]:
				self.min_tracer.append(item)

	def pop(self):
		if self.size == 0: return "Empty stack"
		item = self.array.pop()
		if item == self.min_tracer[-1]:
			self.min_tracer.pop()

	def get_min(self):
		if len(self.min_tracer) == 0: return None
		return self.min_tracer[-1]

	def __str__(self):
		return str(self.array)

class Test(unittest.TestCase):

	def test(self):
		s = Stack()
		for i in [2, 4, 5, 1, 10]:
			s.push(i)
		self.failUnlessEqual(s.get_min(), 1)
		s.pop()
		s.pop()
		self.failUnlessEqual(s.get_min(), 2)

if __name__ == '__main__':
	unittest.main()