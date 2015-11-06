import unittest
from linked_list import *

# time: O(n) space: O(n)
def partition(linked_list, pivot):
    items = []
    for item in linked_list:
        if item >= pivot:
            items.insert(0, item)
        else:
            items.append(item)
    new_linked_list = LinkedList()
    for item in items:
        new_linked_list.insert(item)
    return new_linked_list


def test():
    ll1 = random_list(10, 1)
    new_ll1 = partition(ll1, 5)
    start = False
    for item in new_ll1:
        if start and item < 5:
            print "fail!"
        if item >= 5:
            start = True
    print "Test passed!"

if __name__ == '__main__':
    test()