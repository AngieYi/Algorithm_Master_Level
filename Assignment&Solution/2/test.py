from longest import *

# basic test
print longest([[], 1, []])# handle node
print longest([[[], 1, []], 2, [[], 3, []]]) # regular easy example
print longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])


print longest([[[[[],1,[]],2,[]],3,[]],4,[]]) # always left tree

print longest([[],5,[[],6,[[],7,[[],8,[]]]]]) # always right tree

print longest([[[],0,[]],1,[[[[[],2,[]],3,[]],4,[]],6,[[],7,[[],8,[[],9,[]]]]]])