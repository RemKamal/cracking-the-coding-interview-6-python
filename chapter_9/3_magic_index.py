import unittest

# Time: O(lgN) Space: in-place
def magic_index(array, start = None, end = None, big = 0):
	if array == []: return -1

	if start == None:
		start = 0
	if end == None:
		end = len(array) - 1

	if start > end:
		return -1

	mid = (start + end) / 2
	if mid == array[mid]:
		return mid

	if mid < array[mid]:
		return magic_index(array, start = start, end = mid - 1)
	else:
		return magic_index(array, start = mid + 1, end = end)


class Test(unittest.TestCase):

	def test(self):
		array1 = [0, 1, 2, 3, 4, 5, 6]
		array2 = [0, 2, 3, 4, 5, 8]
		array3 = [1, 2, 3, 4]
		array4 = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10]

		self.failUnlessEqual(magic_index(array1), 3)
		self.failUnlessEqual(magic_index(array2), 0)
		self.failUnlessEqual(magic_index(array3), -1)
		self.failUnlessEqual(magic_index(array4), 4)

if __name__ == '__main__':
	unittest.main()