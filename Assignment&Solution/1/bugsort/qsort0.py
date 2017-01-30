# CS519_HW1
# Name: Hongyan Yi
# ONID: yih

# this is a buggy version of qsort which is weird in an interesting way:
# it actually returns a binary search tree for the given array, rooted at the pivot:

def sort(a):
	if a == []:
		return []
	else:
		pivot = a[0]
		left = [x for x in a if x < pivot ]
		right = [x for x in a[1:] if x >= pivot]
		return [sort(left)] + [pivot] + [sort(right)]  # buggy part

'''
test scenario
>>> from qsort import *
>>> tree = sort([4,2,6,3,5,7,1,9])
>>> tree
[[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]
>>> sorted(tree)
[1, 2, 3, 4, 5, 6, 7, 9]
>>> search(tree, 6)
True
>>> search(tree, 6.5)
False
>>> insert(tree, 6.5)
>>> tree
[[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[[], 6.5, []], 7, [[], 9, []]]]]
>>> insert(tree, 3)
>>> tree
[[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[[], 6.5, []], 7, [[], 9, []]]]]
'''

# sorted(t): returns the sorted order of one binary search tree(infix traversal)
def sorted(a):
	if a == []:
		return [] 
	else:
		if (a[0] == []) and (a[2] == []):
			return [a[1]]
		else:
			return sorted(a[0]) + [a[1]] + sorted(a[2])	# time complexity: T(n) = 2T(n)+O(1) O(n^log2)



# helper function which returns the subtree (a list) rooted at x when x is found, or the [] when x should be inserted.
def search0(a, x):
	if a == []:
		return []
	else:
		if x == a[1]:
			return a
		elif x > a[1]:
			return search0(a[2],x)	# time complexity: T(n) = T(n)+O(1)   O(nlogn)
		else:
			return search0(a[0],x)


	
# search(t, x): returns whether x is in t
def search(a,x):
	value = search0(a,x)	# time complexity: O(nlogn)
	if value == []:
		return False
	else:
		return True



# insert(t, x): inserts x into t (in-place) if it is missing, otherwise does nothing.
def insert(a,x):
	value = search0(a,x)
	if value == []:
		if a == []:
			return [[],x,[]]
		if x > a[1]:
			return [a[0]]+[a[1]]+[insert(a[2],x)]	# time complexity: T(n) = T(n)+O(nlogn)   O(n(logn)^2)
		else:
			return [insert(a[0],x)]+[a[1]]+[a[2]]	
	else:
		return a