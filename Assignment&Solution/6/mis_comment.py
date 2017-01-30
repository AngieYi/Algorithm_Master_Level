def solution(i, a, back):
    if i < 0:
        return []
    if back[i]:
        return (solution(i-2, a, back) + [a[i]])
    else:
        return solution(i-1, a, back)

def max_wis(a):
    back = {}       # used to record whether this item was used,if used set to true, otherwise it's false.
    n = len(a)

    def top_down(i, opt={-1:0, -2:0}):
        if i in opt:
            return opt[i]
        opt[i] = max(top_down(i-1), top_down(i-2)+a[i])
        back[i] = opt[i] != opt[i-1]
        return opt[i]

    return top_down(n-1), solution(n-1, a, back)

def max_wis2(a):
    opt = {-1: 0, -2: 0}
    back = {}
    n = len(a)
    for i in range(n):
        opt[i] = max(opt[i-1], opt[i-2]+a[i]) 
        back[i] = opt[i] != opt[i-1]
    return opt[n-1], solution(n-1, a, back)


def solution3(i, a, back):
    if i < 0:
        return []

    return solution3(i-1, a, back >> 1) if back & 1 else (solution3(i-2, a, back >> 2) + [a[i]]) # or back%2; note back>>2!

def max_wis3(a): # O(1)-space, with binary number for back
    x, y = 0, 0
    back = 0
    n = len(a)
    for i in range(n):
        x, y = y, max(y, x+a[i])
        back = back * 2 + (x==y)
        #back = back << 1 | (x == y)     # or back = back * 2 + (x==y)
    return y, solution3(n-1, a, back)


print max_wis3([7,4,-5,2])


'''
print max_wis2([7,4,-5,2])
print max_wis([2,7,4,3,-9,8,6,5])
print max_wis([7,8,5])
print max_wis([7,13,5])
print max_wis([-7,-5])
print max_wis([0,-5])

print max_wis2([7,8,5])
print max_wis2([7,13,5])
print max_wis2([-7,-5])
print max_wis2([0,-5])

print max_wis3([7,8,5])
print max_wis3([7,13,5])
print max_wis3([-7,-5])
print max_wis3([0,-5])

print max_wis2([5, 6, 8, -9, 3, 4, 7, 2, 0])
print max_wis3([5, 6, 8, -9, 3, 4, 7, 2, 0])

import sys
from time import time

if __name__ == '__main__':
    #sys.setrecursionlimit(1000000)
    lst = range(800)

    t= time()
    a = max_wis(lst)
    print time() -t

    t= time()
    a = max_wis2(lst)
    print time() -t

    t= time()
    b = max_wis3(lst)
    print time() -t

    print a==b

'''