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
        if (k != -1):
            struct[(i,j)] = final_dict(opt,i,k,struct).copy()    # dictionary could not directly use + to join
            struct[(i,j)].update(final_dict(opt,k+1,j,struct))
            return struct[(i,j)]
        else:
            struct[(i,j)].update(final_dict(opt,i+1,j-1,struct))
            return struct[(i,j)]

'''
tot[i, j] -- total number of structures
pair[i, j] -- total number of structures such that i and j-1 are paired, i.e.,
note that pair[i, j] counts a subset of tot[i, j].

now tot[i, j] involves three cases:
a) i is unpaired -- uses tot[i+1, j]
b) i is paired with j-1 -- uses pair[i+1, j-1]
c) i is paired with k-1 (k<j) -- uses pair[i, k] and tot[k, j]
'''

def total(str):
    valid_set = set(['AU','GC','GU','UA','CG','UG'])
    i = 0
    j = len(str)-1

    struct = defaultdict(lambda:defaultdict(lambda: '.'))
    opt = defaultdict(list)
    tot = defaultdict(int)  # total number of structures
    pair = defaultdict(int) # total number of structures such that i and j-1 are paired


    def _total(str,i,j,struct):
        if (i,j) in opt:
            struct[(i,j)] = struct[(i,j)]
            return opt[(i,j)][0][0]
        if i == j:
            opt[(i,j)] = [(0,-1)]
            struct[(i,j)][i] = '.'
            return 0
        if i + 1 == j:  # only two elements
             tmp2 = str[i]+str[j]
             if tmp2 in valid_set:
                struct[(i,j)][i] = '('
                struct[(i,j)][j] = ')'
                opt[(i,j)] = [(1,-1)]
                return 1
             else:
                struct[(i,j)][i] = '.'
                struct[(i,j)][j] = '.'
                opt[(i,j)] = [(0,-1)]
                return 0
        tmp1 = str[i]+str[j]
        if tmp1 in valid_set:
            struct[(i,j)][i] = '('
            struct[(i,j)][j] = ')'
            opt[(i,j)].append((1 + _total(str,i+1,j-1,struct),-1))
        for k in xrange(i,j):
            opt[(i,j)].append((_total(str,i,k,struct) + _total(str,k+1,j,struct),k))
        # if(i == 0 and j == len(str)-1):
        #     print "before max",opt[(0,len(str)-1)]
        length = 0
        for (pair,split) in opt[(i,j)]:
            if pair != 0:
                length += 1
        opt[(i,j)].append((length,float("inf")))
        # if(i == 0 and j == len(str)-1):
        #     print "after max",opt[(0,len(str)-1)]
        return tot[i,j]

    return (_total(str,i,j,struct),solution(final_dict(opt,i,j,struct)))
    # return (choice(str,i,j,struct))


# print total("AC")
# print total("GUAC")
print total("GCACG")
# print total("CCGG")
# print total("CCCGGG")
# print total("UUCAGGA")
# print total("AUAACCUA")
# print total("UUGGACUUG")
# print total("UUUGGCACUA")
# print total("GAUGCCGUGUAGUCCAAAGACUUC")
# print total("AGGCAUCAAACCCUGCAUGGGAGCG")
# #(2, '((.))')
# print total("UUCAGGA")
# #(3, '(((.)))')
# print total("GUUAGAGUCU")
# #(4, '(.()((.)))')
# print total("GCACG")
# # #(2, '().()')
# print total("AUAACCUUAUAGGGCUCUG")
# #(8, '.(((..)()()((()))))')
# print total("UUGGACUUGAGAAAAG")
# #(5, '((...((()))...))')
# print total("UCAAUGGGUAGUAAAU")
# #(6, '(((.)))((..(.)))')
# print total("UUUGGCACUUUCAGA")
# # (6, '(((((.(..))))))')
# print total("ACACACCUUGUCCGUGAA")
# # (6, '.((.(..)))(.()(.))')
# print total("GAUGCCGUGUAGUCCAAAGACUUCACCGUUGG")
# # (14, '.()()(()(()())(((.((.)(.))()))))')
# print total("CGCGAAUAAAAAGGCACUGUU")
# # (8, '()()((((....(().)))))')
# print total("ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC")
# # (19, '.()(((.)(..))(((.()()(())))(((.)((())))))())')
# print total("UGGGUGAGUCGCACACUCUGCGUACUCUUUCCGUAAUU")
# # (15, '.((()((((.()).(.)))(()())).((...()))))')
# print total("AUACGUCGGGGACAAGAAUUACGG")
# # (8, '.(.(((()((..(..)..))))))')
# print total("AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA")
# # (20, '.(()())...((((()()))((()(.()(((.)))()())))))()')
# print total("CGAGGUGGCACUGACCAAACACCACCGAAAC")
# # (9, '.(.((((().)((.)..))).)...()...)')
# print total("CGCCGUCCGGGCGCGCCUUUUACGUAGAUUU")
# # (12, '.(..(...((((())))(((.(())))))))')
# print total("CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU")
# # (18, '(()())(((((.)))()(((())(.(.().()()))))))')
# print total("AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU")
# # (11, '(((.(..(.((.)((...().))()))))))')
#
#
# print total("GGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA")
# print total("CCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA")
# print total("CUGCAUGG")
# print total("GCAU")
# print total("GAGCACCGCCACUGGCGAUUUU")