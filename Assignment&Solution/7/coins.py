from collections import defaultdict
'''
did not finish
'''
# O(nx) time; O(nx) space
def best(W, items):
    n = len(items)
    back = defaultdict(int)

    def _best(x, i, opt=defaultdict(int)):
        if i < 0 or (x, i) in opt:
            return opt[x, i]

        w = items[i]
        xx = x
        for j in xrange(W/2):   # maximum W/2 items
            if xx == 0:        # empty bag
                break
            ans = _best(xx, i-1) + 1
            if ans < opt[x, i]:
                opt[x, i] = ans
                back[x, i] = j
            xx -= w
        return opt[x, i]

    return _best(W, n-1), solution(W, n-1, back, items)

def solution(x, i, back, items):
    if i < 0:
        return []
    j = back[x, i]
    w = items[i]
    return solution(x - w*j, i-1, back, items) + [j]

#print best(3, [(2, 4, 2), (3, 5, 3)])
print best(47, [6, 10, 15]) # (3, [2, 2, 1])
print best(59, [6, 10, 15]) # (3, [4, 2, 1])
print best(37, [4, 6, 15])  #(3, [4, 1, 1])
print best(27, [4, 6, 15])  #(2, [3, 0, 1])
print best(75, [4, 6, 15])  #(1, [0, 0, 5])
print best(17, [2, 4, 6])   # None


