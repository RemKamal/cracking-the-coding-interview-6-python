import unittest
from linked_list import *

# time: O(n) space: O(n)
def palindrome(linked_list):
    n = len(linked_list)
    i = -1
    half = []
    for item in linked_list:
        if i < n / 2 - 1:
            i += 1
            half.append(item)
        elif n % 2 != 0:
            pass
        elif half[i] != item:
            return False
        else:
            i -= 1
    return True

class Test(unittest.TestCase):

    def test(self):
        ll1 = LinkedList()
        for i in [1, 0, 0, 1]:
            ll1.insert(i)
        ll2 = LinkedList()
        for i in [1, 0, 1]:
            ll2.insert(i)
        ll3 = random_list(10)

        self.assertTrue(palindrome(ll1))
        self.assertTrue(palindrome(ll2))
        self.assertFalse(palindrome(ll3))

if __name__ == '__main__':
    unittest.main()