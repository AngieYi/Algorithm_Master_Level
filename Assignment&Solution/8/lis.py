from collections import defaultdict
from heapq import heappush, heappop

def solution(j, a, opt):# time cost O(2*logn)
    lst = []            # space cost O(n)
    final_str = ""
    pre = opt[j][1]
    while pre != -1:
        heappush(lst,a[pre])
        pre = opt[pre][1]
    while len(lst)!= 0:
        final_str += heappop(lst)
    return final_str

def lis(str):
    a = str + "{"
    j = len(a) - 1
    opt = defaultdict(int)
    opt[0] = (1, -1) # space cost O(n)

    def _lis(j, a, opt):
        tmp = [(1, -1)]             # each recursive call, cost space cost O(n)
        if j in opt:
            return opt[j][0]
        for i in xrange(j-1,-1,-1):     # time cost O(n^2)
            if a[i] < a[j]:
                tmp.append((_lis(i, a, opt)+1, i))
        opt[j] = max(tmp)
        return opt[j][0]

    _lis(j, a, opt)
    return solution(j, a, opt)

if __name__ == '__main__':
    print lis("aebbcg")
    print lis("zyx")
    print lis("aebbdgc")
    print lis("bbabcd")
    print lis("aabbaa")
    print lis("aaa")
    print lis("56234199895")
    print lis("efcdab")
    print lis("56781234")

