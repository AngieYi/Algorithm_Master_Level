from collections import defaultdict
from heapq import heappush,heappop
import heapq
from random import randint


def solution(dict):
    struct_str = ''
    for x in xrange(0,len(dict)):
        struct_str += dict[x]
    return struct_str

def final_dict(opt,i,j,struct):
    if i == j: # only one element
        # struct[(i,j)][i] = '.'
        return struct[(i,j)]
    if i == j + 1:  # (has nothing) has nothing
        # struct[(i,j)][i] = ''
        return struct[(i,j)]
    # for(num,k) in opt[(i,j)]:
    k = opt[(i,j)][0][1]
    if k != -1:
        # struct[(i,j)][i] = '('
        # struct[(i,j)][k] = ')'
        # struct[(i,j)] = final_dict(opt,i+1,k-1,struct).copy()    # dictionary could not directly use + to join
        # struct[(i,j)].update(final_dict(opt,k+1,j,struct))
        return solution(struct[(i,j)][i])+solution(struct[(i+1,k-1)])+solution(struct[(i,j)][j])+solution(struct[(k+1,j)])
    else:
        struct[(i,j)].update(final_dict(opt,i+1,j,struct))
        return solution(struct[(i+1,j)])


def qselect(k, a):
    if a == [] or k < 1 or k > len(a):
        return None
    else:
        pindex = randint(0, len(a)-1)
        a[0],a[pindex] = a[pindex],a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        lleft = len(left)
        return pivot if k == lleft+1 else \
            qselect(k, left) if k <= lleft else \
            qselect(k-lleft-1, right)

print qselect(2, [3, 10, 4, 7, 19])


def kbest(str,num):
    valid_set = set(['AU','GC','GU','UA','CG','UG'])
    i = 0
    j = len(str)-1
    heap = defaultdict(list)

    struct = defaultdict(lambda: defaultdict(lambda: '.'))
    opt = defaultdict(list)
    final_list = []

    def _kbest(str,i,j,struct):
        if (i,j) in opt:
            struct[(i,j)] = struct[(i,j)]
            return opt[(i,j)][0][0]
        if i == j:      # one element
            opt[(i,j)].append((0,-1))
            struct[(i,j)][i] = '.'
            return 0
        if i == j + 1:  # (has nothing) has nothing
            opt[(i,j)].append((0,-1))
            # struct[(i,j)][i] = ''
            return 0
        opt[(i,j)].append((_kbest(str,i+1,j,struct),-1))     # assume first element is "."
        for k in xrange(i+1,j+1):   # assume first element is "(",check whether has ")" to pair
            if str[i]+str[k] in valid_set:
                struct[(i,j)][i] = '('
                struct[(i,j)][k] = ')'
                opt[(i,j)].append((_kbest(str,i+1,k-1,struct)+_kbest(str,k+1,j,struct),k))
        opt[(i,j)].sort(reverse=True)
        for x in xrange(0,num):
            # final_list.append((opt[(i,j)][x][0],k))
            if x < len(opt[(i,j)]):
                heap[(i,j)].append((opt[(i,j)][x][0],k))
                # heappush(heap[(i,j)],(opt[(i,j)][x][0],k))
            else:
                break

        # sorted(opt[(i,j)])
        # print opt[(i,j)]
        # opt[(i,j)] = [max(opt[(i,j)])]
        # one_best = max(opt[(i,j)])[0]
        return opt[(i,j)][0][0]

    _kbest(str,i,j,struct)

    # return _kbest(str,i,j,struct),heap[(i,j)]
    return heap[(i,j)]


# print kbest("CG")
# print kbest("G")
# print kbest("GG")


print kbest("ACAGU",10)
# print kbest("AC")
# print kbest("GUAC")
# print kbest("GCACG")
# print kbest("CCGG")
# print kbest("CCCGGG")
# print kbest("UUCAGGA")
# print kbest("AUAACCUA")
# print kbest("UUGGACUUG")
# print kbest("UUUGGCACUA")
# print kbest("GAUGCCGUGUAGUCCAAAGACUUC")
# print kbest("AGGCAUCAAACCCUGCAUGGGAGCG")