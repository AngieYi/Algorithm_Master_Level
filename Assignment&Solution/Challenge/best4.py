'''
best("ACAGU")
(2, '((.))')
'''
from collections import defaultdict

def solution(opt2,i,j,structure2):
    start = i
    end = j
    while(i <= j):
        k = opt2[(i,j)][0][1]
        if (k != -1):
            structure2[(i,j)] = structure2[(i,k)].copy() # dictionary could not directly use + to join
            structure2[(i,j)].update(structure2[(k+1,j)])
        else:
            structure2[(i,j)].update(structure2[(i+1,j-1)])
            i += 1
            j -= 1
    struct_str = ''
    for x in xrange(0,len(structure2[start,end])):
        struct_str += dict[x]
    return struct_str


def best(str):
    valid_set = set(['AU','GC','GU','UA','CG','UG'])
    i = 0
    j = len(str)-1

    structure2 = defaultdict(lambda:defaultdict(lambda: "."))
    inner_structure = defaultdict(lambda: ".")
    opt2 = defaultdict(list)

    def choice(str,i,j,inner_structure):
        if (i,j) in opt2:
            inner_structure = structure2[(i,j)]
            return opt2[(i,j)][0][0]
        if i == j:
            opt2[(i,j)] = [(0,i)]
            inner_structure[i] = '.'
            return 0
        if i > j:
            return 0
        if i + 1 == j:
             tmp2 = str[i]+str[j]
             if tmp2 in valid_set:
                inner_structure[i] = '('
                inner_structure[j] = ')'
                opt2[(i,j)] = [(1,i+1)]
                return 1
             else:
                inner_structure[i] = '.'
                inner_structure[j] = '.'
                opt2[(i,j)] = [(0,i+1)]
                return 0
        tmp1 = str[i]+str[j]
        if tmp1 in valid_set:
            structure2[(i,j)][i] = '('
            structure2[(i,j)][j] = ')'
            opt2[(i,j)].append((1 + choice(str,i+1,j-1,structure2[(i+1,j-1)]),-1))
        else:
            for k in xrange(i,j):
                opt2[(i,j)].append((choice(str,i,k,structure2[(i,k)]) + choice(str,k+1,j,structure2[(k+1,j)]),k))
        opt2[(i,j)] = [max(opt2[(i,j)])]

        return opt2[(i,j)][0][0]

    return (choice(str,i,j,inner_structure),solution(opt2,structure2))

print best("ACAGU")
# print best("UUCAGGA")
# print best("GUUAGAGUCU")
# print best("GCACG")
# print best("AUAACCUUAUAGGGCUCUG")
# print best("UUGGACUUGAGAAAAG")
# print best("UCAAUGGGUAGUAAAU")



