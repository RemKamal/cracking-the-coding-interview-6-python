import unittest
from linked_list import *

# time: O(n) space: O(n)
def sum_list(ll1, ll2):
    n1, n2 = len(ll1), len(ll2)
    i, j = n1, n2
    num1, num2 = 0, 0
    for digit in ll1:
        num1 += 10 ** (n1 - i) * digit
        i -= 1
    for digit in ll2:
        num2 += 10 ** (n2 - j) * digit
        j -= 1
    result = LinkedList()
    for digit in str(num1 + num2):
        result.insert(int(digit))
    return result

class Test(unittest.TestCase):

    def test(self):
        ll1 = LinkedList()
        for i in [4, 3, 0]:
            ll1.insert(i)
        ll2 = LinkedList()
        for i in [1, 0, 0]:
            ll2.insert(i)
        ll = LinkedList()
        for i in [5, 3, 0]:
            ll.insert(i)

        self.assertTrue(sum_list(ll1, ll2) == ll)

if __name__ == '__main__':
    unittest.main()