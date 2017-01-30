'''
best("ACAGU")
(2, '((.))')
'''
from collections import defaultdict

def solution(dict):
    struct_str = ''
    for x in xrange(0,len(dict)):
        struct_str += dict[x]
    return struct_str


def best(str):
    valid_set = set(['AU','GC','GU','UA','CG','UG'])
    i = 0
    j = len(str)-1

    structure1 = defaultdict(lambda:".")
    structure2 = defaultdict(lambda:defaultdict(lambda: "."))
    inner_structure = defaultdict(lambda: ".")
    opt2 = defaultdict(list)

    def choice1(str,i,j,structure1):
        if i == j:
            structure1[i] = "."
            return 0
        if i > j:
            return 0
        tmp1 = str[i]+str[j]
        if tmp1 in valid_set:
            structure1[i] = '('
            structure1[j] = ')'
            i += 1
            j -= 1
            opt1 = 1 + choice1(str,i,j,structure1)
        else:
            structure1[i] = '.'
            structure1[j] = '.'
            i += 1
            j -= 1
            opt1 = choice1(str,i,j,structure1)
        return opt1

    def choice2(str,i,j,inner_structure):
        if (i,j) in opt2:
            inner_structure = structure2[(i,j)]
            return opt2[(i,j)][0][0]
        if i == j:
            opt2[(i,j)] = [(0,i)]
            inner_structure[i] = '.'
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
        for k in xrange(i,j):
            opt2[(i,j)].append((choice2(str,i,k,structure2[(i,k)]) + choice2(str,k+1,j,structure2[(k+1,j)]),k))
        opt2[(i,j)] = [max(opt2[(i,j)])]
        k = opt2[(i,j)][0][1]
        structure2[(i,j)] = structure2[(i,k)].copy() # dictionary could not directly use + to join
        structure2[(i,j)].update(structure2[(k+1,j)])
        return opt2[(i,j)][0][0]

    x = choice1(str,i,j,structure1)
    y = choice2(str,i,j,inner_structure)
    if (x >= y):
        print "choice1"
        return (x,solution(structure1))
    else:
        print "choice2"
        return (y,solution(structure2[(i,j)]))

# print best("ACAGU")
# print best("UUCAGGA")
print best("GAGUC")
print best("UUAGAGUC")
print best("GUUAGAGUCU")



