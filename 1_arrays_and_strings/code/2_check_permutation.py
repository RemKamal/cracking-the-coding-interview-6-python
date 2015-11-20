import unittest

# time: O(n) space: O(n)
def check_perm(a, b):
	if len(a) != len(b): return False

	checker = {}
	for letter in a:
		if letter in checker:
			checker[letter] += 1
		else:
			checker[letter] = 1

	for letter in b:
		if letter not in checker:
			return False
		else:
			if checker[letter] <= 0:
				return False
			checker[letter] -= 1
	return True


class Test(unittest.TestCase):

	def test(self):
		self.assertTrue(check_perm('abcd', 'acdb'))
		self.assertFalse(check_perm('abcns', 'as'))
		self.assertFalse(check_perm('mnbvc', 'zxcvb'))
		self.assertFalse(check_perm('aabbcc', 'abcccc'))


if __name__ == "__main__":
	unittest.main()