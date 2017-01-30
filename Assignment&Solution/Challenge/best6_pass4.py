from collections import defaultdict

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


# print best("CG")

print best("ACG")

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
# #(2, '((.))')

print best("UUCAGGA")
#(3, '(((.)))')
print best("GUUAGAGUCU")
#(4, '(.()((.)))')
print best("GCACG")
# #(2, '().()')
print best("AUAACCUUAUAGGGCUCUG")
#(8, '.(((..)()()((()))))')
print best("UUGGACUUGAGAAAAG")
#(5, '((...((()))...))')
print best("UCAAUGGGUAGUAAAU")
#(6, '(((.)))((..(.)))')
print best("UUUGGCACUUUCAGA")
# (6, '(((((.(..))))))')
print best("ACACACCUUGUCCGUGAA")
# (6, '.((.(..)))(.()(.))')
print best("GAUGCCGUGUAGUCCAAAGACUUCACCGUUGG")
# (14, '.()()(()(()())(((.((.)(.))()))))')
print best("CGCGAAUAAAAAGGCACUGUU")
# (8, '()()((((....(().)))))')
print best("ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC")
# (19, '.()(((.)(..))(((.()()(())))(((.)((())))))())')
print best("UGGGUGAGUCGCACACUCUGCGUACUCUUUCCGUAAUU")
# (15, '.((()((((.()).(.)))(()())).((...()))))')
print best("AUACGUCGGGGACAAGAAUUACGG")
# (8, '.(.(((()((..(..)..))))))')
print best("AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA")
# (20, '.(()())...((((()()))((()(.()(((.)))()())))))()')
print best("CGAGGUGGCACUGACCAAACACCACCGAAAC")
# (9, '.(.((((().)((.)..))).)...()...)')
print best("CGCCGUCCGGGCGCGCCUUUUACGUAGAUUU")
# (12, '.(..(...((((())))(((.(())))))))')
print best("CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU")
# (18, '(()())(((((.)))()(((())(.(.().()()))))))')
print best("AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU")
# (11, '(((.(..(.((.)((...().))()))))))')
#
#
# print best("GGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA")
# print best("CCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA")
# print best("CUGCAUGG")
# print best("GCAU")
# print best("GAGCACCGCCACUGGCGAUUUU")