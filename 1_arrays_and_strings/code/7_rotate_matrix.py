import unittest

def rotate(matrix):
	return zip(*matrix[::-1])

class Test(unittest.TestCase):

	def test(self):
		testset1 = [
				   	[('a', 'b'), ('c', 'd')],
				   	[('c', 'a'), ('d', 'b')]
				   ]

		testset2 = [
					[('a', 'b', 'c'),
					 ('1', '2', '3'),
					 ('#', '$', '*')],

					[('#', '1', 'a'),
					 ('$', '2', 'b'),
					 ('*', '3', 'c')]
				   ]
		self.failUnlessEqual(rotate(testset1[0]), testset1[1])
		self.failUnlessEqual(rotate(testset2[0]), testset2[1])

if __name__ == '__main__':
	unittest.main()