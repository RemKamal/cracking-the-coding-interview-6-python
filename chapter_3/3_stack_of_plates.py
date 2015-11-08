import unittest

class StackPlate():
	"""
		Space: O(n)
		Push: O(1)
		Pop: O(1)
		Pop_at: O(1)
	"""

	def __init__(self, limit = 5):
		self.limit = limit
		self.stacks = [[]]
		self.stack_id = 0

	def push(self, item):
		if len(self.stacks[self.stack_id]) >= self.limit:
			self.stack_id += 1
			self.stacks.append([])
			self.stacks[self.stack_id].append(item)
		else:
			self.stacks[self.stack_id].append(item)

	def pop(self):
		if self.stacks[0] == []: return None
		if self.stacks[self.stack_id] == []:
			self.stack_id -= 1
			self.stacks[self.stack_id].pop()
		else:
			self.stacks[self.stack_id].pop()

	def pop_at(self, stack_id):
		if self.stacks[stack_id] == []: return None
		self.stacks[stack_id].pop()

	def __str__(self):
		result = ""
		for i in range(self.stack_id + 1):
			result += "Stack ID: {}, {}\n".format(i, self.stacks[i])
		return result

class Test(unittest.TestCase):

	def test(self):
		ss = StackPlate()
		for i in range(10, 34):
			ss.push(i)
		ss.pop()
		ss.pop_at(0)

		array = [[10, 11, 12, 13], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24], [25, 26, 27, 28, 29], [30, 31, 32]]

		self.failUnlessEqual(ss.stacks, array)

if __name__ == '__main__':
	unittest.main()