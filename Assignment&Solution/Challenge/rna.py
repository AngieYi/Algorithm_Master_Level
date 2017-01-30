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

def total(str):
    valid_set = set(['AU','GC','GU','UA','CG','UG'])
    start = 0
    end = len(str)-1
    opt = defaultdict(int)

    def _total(str,start,end):
        if (start,end) in opt:
            return opt[(start,end)]
        num_struct = 0
        if start == end:      # one element
            return 1
        if start == end + 1:  # (has nothing) after has nothing
            return 1
        num_struct += _total(str,start+1,end)
        for k in xrange(start+1,end+1):
            if str[start]+str[k] in valid_set:
                num_struct += _total(str,start+1,k-1) * _total(str,k+1,end)
        opt[(start,end)] = num_struct
        return num_struct

    return _total(str,start,end)


# print total("CG")
# print total("C")
# print total("GG")
# print total("CGG")


print total("ACAGU")
print total("AC")
print total("GUAC")
print total("GCACG")
print total("CCGG")
print total("CCCGGG")
print total("UUCAGGA")
print total("AUAACCUA")
print total("UUGGACUUG")
print total("UUUGGCACUA")
print total("GAUGCCGUGUAGUCCAAAGACUUC")
print total("AGGCAUCAAACCCUGCAUGGGAGCG")

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