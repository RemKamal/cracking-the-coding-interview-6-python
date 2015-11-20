import unittest

# time: O(n) space: in-place
def urlify(s):
	return '%20'.join(s.split())

class Test(unittest.TestCase):

	def test(self):
		self.failUnlessEqual(urlify('yy for the win  '), 'yy%20for%20the%20win')

if __name__ == '__main__':
	unittest.main()