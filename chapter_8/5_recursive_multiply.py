import unittest

def rec_multiply(a, b):
	if b == 0: return 0
	if b == 1: return a

	halven = b >> 1
	half = rec_multiply(a, halven)

	if b % 2 == 1:
		return half + half + a
	else:
		return half + half

class Test(unittest.TestCase):

	def test(self):
		self.failUnlessEqual(rec_multiply(10, 0), 0)
		self.failUnlessEqual(rec_multiply(0, 10), 0)
		self.failUnlessEqual(rec_multiply(10, 10), 100)
		self.failUnlessEqual(rec_multiply(20, 5), 100)

if __name__ == '__main__':
	unittest.main()
