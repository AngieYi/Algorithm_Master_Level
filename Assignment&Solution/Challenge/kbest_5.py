from collections import defaultdict
from heapq import heappush,heappop

def solution(dict):
    struct_str = ''
    for x in xrange(0,len(dict)):
        struct_str += dict[x]
    return struct_str

def final_dict_kbest(opt,i,j,struct):
    if i == j: # only one element
        return solution(struct[(i,j)])
    if i == j + 1:  # (has nothing) has nothing
        return solution(struct[(i,j)])
    k = opt[(i,j)][0][2]
    if k != -1:
        # struct[(i,j)] = final_dict(opt,i+1,k-1,struct).copy()    # dictionary could not directly use + to join
        # struct[(i,j)].update(final_dict(opt,k+1,j,struct))
        return "(" + solution(struct[(i+1,k-1)]) + ")" + solution(struct[(k+1,j)])
        # return solution(struct[(i,j)][i]) + solution(struct[(i+1,k-1)]) + solution(struct[(i,j)][j]) + solution(struct[(k+1,j)])
    else:
        # struct[(i,j)].update(final_dict_kbest(opt,i+1,j,struct))
        return "." + solution(struct[(i+1,j)])

def kbest(str,num):
    valid_set = set(['AU','GC','GU','UA','CG','UG'])
    i = 0
    j = len(str)-1
    final_list = []

    struct = defaultdict(lambda: defaultdict(lambda: '.'))
    opt = defaultdict(list)
    heap = defaultdict(list)

    def _kbest(str,i,j,struct):
        if i == j:      # one element
            heappush(heap[(i,j)],(0,'C',-1))
            opt[(i,j)].append((0,'C',-1))
            struct[(i,j)][i] = '.'
            return 0
        if i == j + 1:  # (has nothing) has nothing
            heappush(heap[(i,j)],(0,'C',-1))
            opt[(i,j)].append((0,'C',-1))
            struct[(i,j)][i] = ''
            return 0

        heappush(heap[(i,j)],(-_kbest(str,i+1,j,struct),'A',-1)) # assume first element is "."

        for k in xrange(i+1,j+1):   # assume first element is "(",check whether has ")" to pair
            if str[i]+str[k] in valid_set:
                struct[(i,j)][i] = '('
                struct[(i,j)][k] = ')'
                heappush(heap[(i,j)],(-1-_kbest(str,i+1,k-1,struct)-_kbest(str,k+1,j,struct),'B',k))
                heappush(heap[(i,j)],(-_kbest(str,i+1,k-1,struct),'L',k))
                heappush(heap[(i,j)],(-_kbest(str,k+1,j,struct),'R',k))

        for x in xrange(0,num):
            if x < len(heap[(i,j)]):
                for (n,_,k) in [heappop(heap[(i,j)])]:
                    opt[(i,j)].append((-n,_,k))
            else:
                break
        return opt[(i,j)][0][0]

    _kbest(str,i,j,struct)

    for x in xrange(0,num):
        if x < len(opt[(i,j)]):
            final_list.append((opt[(i,j)][x][0],final_dict_kbest(opt,i,j,struct)))

    return final_list


# print kbest("G",10)
# print kbest("CG",10)
# print kbest("ACG",10)
# print kbest("CACG",10)
# print kbest("GCACG",10)

# print kbest("GG",10)
#
# print kbest("ACAGU",10)
# #[(2, '((.))'), (1, '.(.).'), (1, '..(.)'), (1, '...()'), (1, '(...)'), (0, '.....')]
# print kbest("AC",10)
# print kbest("GUAC",10)

print kbest("GCACG",10)
# #[(2, '().()'), (1, '(..).'), (1, '()...'), (1, '.(..)'), (1, '...()'), (0, '.....')]

# print kbest("CCGG",10)
# print kbest("CCCGGG",10)
# print kbest("UUCAGGA",10)
# print kbest("AUAACCUA",10)
# print kbest("UUGGACUUG",10)
# print kbest("UUUGGCACUA",10)
# print kbest("GAUGCCGUGUAGUCCAAAGACUUC",10)
# print kbest("AGGCAUCAAACCCUGCAUGGGAGCG",10)