from collections import defaultdict
from heapq import heappush,heappop

def solution(dict):
    struct_str = ''
    for x in xrange(0,len(dict)):
        struct_str += dict[x]
    return struct_str

def final_dict(opt,i,j,struct):
    if i == j:  # only one element
        return struct[(i,j)]
    if i + 1 == j:  # only two elements
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

def total(str):
    valid_set = set(['AU','GC','GU','UA','CG','UG'])
    i = 0
    j = len(str)-1
    opt = defaultdict(int)

    def _total(str,i,j):
        if (i,j) in opt:
            return opt[(i,j)]
        if i == j:      # one element
            return 1
        if i == j + 1:  # (has nothing) has nothing
            return 1
        opt[(i,j)] += _total(str,i+1,j)
        for k in xrange(i+1,j+1):
            if str[i]+str[k] in valid_set:
                opt[(i,j)] += _total(str,i+1,k-1) * _total(str,k+1,j)
        return opt[(i,j)]

    return _total(str,i,j)


def final_dict_kbest(opt,i,j,struct):
    if i == j:      # only one element
        return solution(struct[(i,j)])
    if i == j + 1:  # (has nothing) has nothing
        return solution(struct[(i,j)])
    k = opt[(i,j)][0][2]
    if k != -1:
        return "(" + solution(struct[(i+1,k-1)]) + ")" + solution(struct[(k+1,j)])
    else:
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
        if (i,j) in opt:
            return opt[(i,j)][0][0]
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

# print total("CG")
# print total("C")
# print total("GG")
# print total("CGG")


# print total("ACAGU")
# print total("AC")
# print total("GUAC")
# print total("GCACG")
# print total("CCGG")
# print total("CCCGGG")
# print total("UUCAGGA")
# print total("AUAACCUA")
# print total("UUGGACUUG")
# print total("UUUGGCACUA")
# print total("GAUGCCGUGUAGUCCAAAGACUUC")
# print total("AGGCAUCAAACCCUGCAUGGGAGCG")

'''
#(2, '((.))')
print total("UUCAGGA")
#(3, '(((.)))')
print total("GUUAGAGUCU")
#(4, '(.()((.)))')
print total("GCACG")
# #(2, '().()')
print total("AUAACCUUAUAGGGCUCUG")
#(8, '.(((..)()()((()))))')
print total("UUGGACUUGAGAAAAG")
#(5, '((...((()))...))')
print total("UCAAUGGGUAGUAAAU")
#(6, '(((.)))((..(.)))')
print total("UUUGGCACUUUCAGA")
# (6, '(((((.(..))))))')
print total("ACACACCUUGUCCGUGAA")
# (6, '.((.(..)))(.()(.))')
print total("GAUGCCGUGUAGUCCAAAGACUUCACCGUUGG")
# (14, '.()()(()(()())(((.((.)(.))()))))')
print total("CGCGAAUAAAAAGGCACUGUU")
# (8, '()()((((....(().)))))')
print total("ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC")
# (19, '.()(((.)(..))(((.()()(())))(((.)((())))))())')
print total("UGGGUGAGUCGCACACUCUGCGUACUCUUUCCGUAAUU")
# (15, '.((()((((.()).(.)))(()())).((...()))))')
print total("AUACGUCGGGGACAAGAAUUACGG")
# (8, '.(.(((()((..(..)..))))))')
print total("AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA")
# (20, '.(()())...((((()()))((()(.()(((.)))()())))))()')
print total("CGAGGUGGCACUGACCAAACACCACCGAAAC")
# (9, '.(.((((().)((.)..))).)...()...)')
print total("CGCCGUCCGGGCGCGCCUUUUACGUAGAUUU")
# (12, '.(..(...((((())))(((.(())))))))')
print total("CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU")
# (18, '(()())(((((.)))()(((())(.(.().()()))))))')
print total("AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU")
# (11, '(((.(..(.((.)((...().))()))))))')


print total("GGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA")
print total("CCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA")
print total("CUGCAUGG")
print total("GCAU")
print total("GAGCACCGCCACUGGCGAUUUU")
'''