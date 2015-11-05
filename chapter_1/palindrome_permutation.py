import unittest

# time: O(n) space: O(n)
def pal_perm(s):
	s = s.replace(" ", "")
	letters = unify_letter(s)
	state = sum(letters.values())

	if state < len(letters) - 1: return False
	elif state == len(letters) and len(s) %2 == 0: return True
	elif state == len(letters) - 1 and len(s) % 2 != 0: return True
	else:
		return False

#  use XOR to change the odd/even state of the counts of a letter
def unify_letter(s):
	checker = {}
	for letter in s:
		letter = letter.lower()
		if letter in checker:
			checker[letter] ^= 1
		else:
			checker[letter] = 0
	return checker

class Test(unittest.TestCase):

	def test(self):
		self.assertTrue(pal_perm('Tact Coa'))
		self.assertTrue(pal_perm('a'))
		self.assertFalse(pal_perm('ab'))
		self.assertFalse(pal_perm('abc de'))

if __name__ == '__main__':
	unittest.main()