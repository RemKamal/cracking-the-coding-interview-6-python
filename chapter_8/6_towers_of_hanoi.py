
# http://www.python-course.eu/towers_of_hanoi.php

def move_towers(towers):
	stack1, stack2 = [], []
	n = len(towers)
	hanoi(n, towers, stack1, stack2)
	return towers, stack1, stack2

def hanoi(n, start, mid, end):
	if n > 0:
		hanoi(n - 1, start, end, mid)
		if start:
			end.append(start.pop())
		hanoi(n - 1, mid, start, end)

towers = [4, 3, 2, 1]
print move_towers(towers)