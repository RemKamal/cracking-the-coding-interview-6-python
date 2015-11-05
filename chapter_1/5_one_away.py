import unittest

def one_away(s1, s2):
	if abs(len(s1) - len(s2)) > 1: return False

	if len(s1) < len(s2):
		s1, s2 = s2, s1

	i, j = 0, 0
	found = False
	while i < len(s1) and j < len(s2):
		if s1[i] != s2[j]:
			if found: return False
			found = True
			if len(s1) == len(s2):
				j += 1
			i += 1
		else:
			i += 1
			j += 1
	return True


class Test(unittest.TestCase):

	def test(self):
		self.assertTrue(one_away("yy", "xy"))
		self.assertFalse(one_away("yy", "xx"))
		self.assertTrue(one_away("yy", "yxy"))
		self.assertFalse(one_away("yy", "yxxy"))
		self.assertTrue(one_away("yy", "y"))
		self.assertFalse(one_away("yy", ""))

if __name__ == "__main__":
	unittest.main()