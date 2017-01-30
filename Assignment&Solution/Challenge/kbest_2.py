from collections import defaultdict

def solution(dict):
    struct_str = ''
    for x in xrange(0,len(dict)):
        struct_str += dict[x]
    return struct_str

def final_dict(opt,i,j,struct):
    if i == j:  # only one element
        # struct[(i,j)] = {i: "."}
        return struct[(i,j)]
    if i == j + 1:  # (has nothing) has nothing
        return struct[(i,j)]
    for(num,k) in opt[(i,j)]:
        # k = opt[(i,j)][0][1]
        if k != -1:
            # struct[(i,j)] = final_dict(opt,i+1,k-1,struct).copy()    # dictionary could not directly use + to join
            # struct[(i,j)].update(final_dict(opt,k+1,j,struct))
            return solution(struct[(i,j)][i])+solution(struct[(i+1,k-1)])+solution(struct[(i,j)][j])+solution(struct[(k+1,j)])
        else:
            struct[(i,j)].update(final_dict(opt,i+1,j,struct))
            return solution(struct[(i+1,j)])

def best(str):
    valid_set = set(['AU','GC','GU','UA','CG','UG'])
    i = 0
    j = len(str)-1

    struct = defaultdict(lambda: defaultdict(lambda: '.'))
    opt = defaultdict(list)

    def _best(str,i,j,struct):
        if (i,j) in opt:
            struct[(i,j)] = struct[(i,j)]
            return opt[(i,j)][0][0]
        if i == j:      # one element
            opt[(i,j)].append((0,-1))
            struct[(i,j)][i] = '.'
            return 0
        if i == j + 1:  # (has nothing) has nothing
            opt[(i,j)].append((0,-1))
            struct[(i,j)][i] = ''
            return 0
        opt[(i,j)].append((_best(str,i+1,j,struct),-1))     # assume first element is "."
        for k in xrange(i+1,j+1):   # assume first element is "(",check whether has ")" to pair
            if str[i]+str[k] in valid_set:
                struct[(i,j)][i] = '('
                struct[(i,j)][k] = ')'
                opt[(i,j)].append((1+_best(str,i+1,k-1,struct)+_best(str,k+1,j,struct),k))
        one_best = max(opt[(i,j)])[0]
        # opt[(i,j)].append((max(opt[(i,j)])[0][0],-2))
        return one_best

    return _best(str,i,j,struct),solution(final_dict(opt,i,j,struct))


print best("CG")
# print best("G")


# print best("ACAGU")
# print best("AC")
# print best("GUAC")
# print best("GCACG")
# print best("CCGG")
# print best("CCCGGG")
# print best("UUCAGGA")
# print best("AUAACCUA")
# print best("UUGGACUUG")
# print best("UUUGGCACUA")
# print best("GAUGCCGUGUAGUCCAAAGACUUC")
# print best("AGGCAUCAAACCCUGCAUGGGAGCG")