from collections import defaultdict

# O(nW) time; O(W) space
def best(W, items):
    back = defaultdict(lambda : -1)
    
    def _best(x, opt=defaultdict(int)):
        if x in opt:
            return opt[x]
        for i, (w, v) in enumerate(items):
            if x >= w:
                ans = _best(x-w) + v
                if ans > opt[x]:
                    opt[x] = ans
                    back[x] = i
        return opt[x]

    return _best(W), solution(W, back, items)

def solution(x, back, items):
    if back[x] == -1:
        return [0] * len(items)
    w, _ = items[back[x]]
    a = solution(x-w, back, items)
    a[back[x]] += 1
    return a

# print best(3, [(2, 4), (3, 5)])
print best(3, [(1, 2), (2, 5)])