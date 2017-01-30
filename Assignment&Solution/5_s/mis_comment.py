# O(n) time & space
def max_wis(a):
    back = {} # not really needed
    n = len(a)

    def top_down(i, best={-1:0, -2:0}):
        if i in best:
            return best[i]
        best[i] = max(top_down(i-1), top_down(i-2)+a[i])
        back[i] = best[i] == best[i-1]
        return best[i]

    return top_down(n-1), solution(n-1, a, back)

def solution(i, a, back):
    if i < 0:
        return []
    return solution(i-1, a, back) if back[i] else (solution(i-2, a, back) + [a[i]])

def max_wis2(a):
    best = {-1: 0, -2: 0}
    back = {}
    n = len(a)
    for i in range(n):
        best[i] = max(best[i-1], best[i-2]+a[i]) 
        back[i] = best[i] == best[i-1]
    return best[n-1], solution(n-1, a, back)


'''
if use array to backtrack, the space complexity will be O(n).
Prof. 's solution uses one integer to save the backtrack information,
this integer you think it as binary number rather than decimal value, for example,
decimal  0   1   2   3     4
binary     0   1  10  11  100
in max_wis3(a) function, it is coding an integer, in solution function it is decoding an integer.
'''
def max_wis3(a): # O(1)-space, O(n) time; with binary number for back
    x, y = 0, 0
    back = 0
    n = len(a)
    for i in range(n):
        x, y = y, max(y, x+a[i])
        #back = back << 1 | (x == y)     # or back = back * 2 + (x==y)
        temp = (x==y)
        # back = back << 1 | temp
        back = back * 2 + temp
    return y, solution3(n-1, a, back)

def solution3(i, a, back):
    if i < 0:
        return []
    if (back & 1):
        return solution3(i-1, a, back >> 1)
    else:
        l_temp = solution3(i-2, a, back >> 2)
        final = l_temp + [a[i]]
        return final # or back%2; note back>>2!

print max_wis3([7,8,5,2])
#print max_wis3([2,7,4,3,-9,8,6,5])

# print max_wis([7,8,5])
# print max_wis([7,13,5])
# print max_wis([-7,-5])
# print max_wis([0,-5])
# print max_wis3([5, 6, 8, -9, 3, 4, 7, 2, 0])
# print
#
# print max_wis2([7,8,5])
# print max_wis2([7,13,5])
# print max_wis2([-7,-5])
# print max_wis2([0,-5])
# print max_wis2([5, 6, 8, -9, 3, 4, 7, 2, 0])

# print max_wis3([7,8,5])
# print max_wis3([7,13,5])
# print max_wis3([-7,-5])
# print max_wis3([0,-5])
# print max_wis3([5, 6, 8, -9, 3, 4, 7, 2, 0])

# import sys
# sys.setrecursionlimit(1000000)
#
# lst = range(10000)
#
# from time import time
# t= time()
# a = max_wis(lst)
# print time() -t
# t= time()
# a = max_wis2(lst)
# print time() -t
# t= time()
# b = max_wis3(lst)
# print time() -t
# print a==b

