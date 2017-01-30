from qselect import *

# check basic correctness
print qselect(2, [3, 10, 4, 7, 19])
print qselect(4, [11, 2, 8, 3])

# handle duplicate
print qselect(4,[1,2,8,3,7,4,5,6,5])
print qselect(5,[1,2,8,3,7,4,5,6,5])
print qselect(6,[1,2,8,3,7,4,5,6,5])
print qselect(7,[1,2,8,3,7,4,5,6,5])

# handle edge case
print qselect(1,[])