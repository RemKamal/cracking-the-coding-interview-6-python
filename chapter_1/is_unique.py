import unittest

# time: O(n), space: in-place
def is_unique(s):
	return len(set(s)) == len(s)

class Test(unittest.TestCase):

	def test(self):
		self.assertTrue(is_unique('abdc'))
		self.assertFalse(is_unique('yyhello'))
		self.assertFalse(is_unique('  **123'))


if __name__ == "__main__":
	unittest.main()