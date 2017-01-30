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
   [UPDATE] a simpler derivation (without pair, thanks to Alex):
   now tot[i, j] involves two cases:
   a) i is unpaired -- uses tot[i+1, j]      i .xxxx j
   b) i is paired with k-1 (i<k<=j) -- uses tot[i+1, k-1] and tot[k, j]
                                             i (xxx) k xxxx j
   note that you can use this division for problem 3, but it's also fine to use
   the overcounting division from problem 1 (but you need to eliminate duplicates).
'''

def total(str):
    valid_set = set(['AU','GC','GU','UA','CG','UG'])
    start = 0
    end = len(str)-1


    def _total(str,start,end):
        num_struct = 1
        num_unpaired = 0
        if start >= end:
            return 0
        for i in xrange(start,end):
            for k in xrange(start+1,end+1):
                if str[i]+str[k] in valid_set:
                    num_struct += _total(str,i+1,k-1) * _total(str,k+1,end)
                else:
                    num_unpaired += 1
                    if num_unpaired == (end - i):
                        num_struct += _total(str,i+1,end)
        return num_struct


    return _total(str,start,end)


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