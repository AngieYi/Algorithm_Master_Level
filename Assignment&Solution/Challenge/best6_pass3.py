from collections import defaultdict

def solution(dict):
    struct_str = ''
    for x in xrange(0,len(dict)):
        struct_str += dict[x]
    return struct_str

def final_dict(opt,i,j,struct):
    if i == j:  # only one element
        struct[(i,j)] = {i: "."}
        return struct[(i,j)]
    if i + 1 == j:  # only two elements
        struct[(i,j)] = struct[(i,j)]
        return struct[(i,j)]
    else:
        k = opt[(i,j)][0][1]
        if k != -1:
            struct[(i,j)] = final_dict(opt,i,k,struct).copy()    # dictionary could not directly use + to join
            struct[(i,j)].update(final_dict(opt,k+1,j,struct))
            return struct[(i,j)]
        else:
            struct[(i,j)].update(final_dict(opt,i+1,j-1,struct))
            return struct[(i,j)]


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
        if i == j:
            opt[(i,j)] = [(0,-1)]
            struct[(i,j)][i] = '.'
            return 0
        if i + 1 == j:
            if str[i]+str[j] in valid_set:
                struct[(i,j)][i] = '('
                struct[(i,j)][j] = ')'
                opt[(i,j)] = [(1,-1)]
                return 1
            else:
                struct[(i,j)][i] = '.'
                struct[(i,j)][j] = '.'
                opt[(i,j)] = [(0,-1)]
                return 0
        if str[i]+str[j] in valid_set:
            struct[(i,j)][i] = '('
            struct[(i,j)][j] = ')'
            opt[(i,j)].append((1 + _best(str,i+1,j-1,struct),-1))
        for k in xrange(i,j):
            opt[(i,j)].append((_best(str,i,k,struct) + _best(str,k+1,j,struct),k))
        opt[(i,j)] = [max(opt[(i,j)])]
        return opt[(i,j)][0][0]

    return _best(str,i,j,struct),solution(final_dict(opt,i,j,struct))

print best("ACAGU")
print best("AC")
print best("GUAC")
print best("GCACG")
print best("CCGG")
print best("CCCGGG")
print best("UUCAGGA")
print best("AUAACCUA")
print best("UUGGACUUG")
print best("UUUGGCACUA")
print best("GAUGCCGUGUAGUCCAAAGACUUC")
print best("AGGCAUCAAACCCUGCAUGGGAGCG")