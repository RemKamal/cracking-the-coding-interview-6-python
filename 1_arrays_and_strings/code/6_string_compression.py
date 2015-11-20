import unittest

# time: O(n) space: O(n)
def compress(s):
	result = []
	count = 1
	for i in range(1, len(s)):
		if s[i - 1] != s[i]:
			result.append(s[i - 1] + str(count))
			count = 1
		else:
			count += 1

	result.append(s[i] + str(count))

	new_s = ''.join(result)

	if len(new_s) >= len(s):
		return s
	else:
		return new_s

class Test(unittest.TestCase):

	def test(self):
		self.failUnlessEqual(compress('aabbbc'), 'aabbbc')
		self.failUnlessEqual(compress('aabbccaa'), 'aabbccaa')
		self.failUnlessEqual(compress('abc'), 'abc')
		self.failUnlessEqual(compress('aabcccccaaa'), 'a2b1c5a3')

if __name__ == "__main__":
	unittest.main()