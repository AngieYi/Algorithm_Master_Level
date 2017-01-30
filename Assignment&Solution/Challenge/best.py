'''
best("ACAGU")
(2, '((.))')
'''
from collections import defaultdict

def best(str):
    valid_set = set(['AU','GC','GU','UA','CG','UG'])
    i = 0
    j = len(str)-1

    structure1 = defaultdict(lambda:".")
    structure2 = defaultdict(lambda:defaultdict("."))
    inner_structure = defaultdict(lambda: ".")
    opt2 = defaultdict(list)

    def choice2(str,i,j,inner_structure):
        if (i,j) in opt2:
            return opt2[(i,j)][0][0]
        if i == j:
            opt2[(i,j)] = [(0,i)]
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
            opt2[(i,j)].append((choice2(str,i,k,structure2[(i,j,k)]) + choice2(str,k+1,j,structure2[(i,j,k)]),k))
        opt2[(i,j)] = [max(opt2[(i,j)])]
        return opt2[(i,j)][0][0]


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


    # opt1 = choice1(str,i,j,structure1)
    choice2(str,i,j,inner_structure)
    # max = max(opt1,opt2)
    return opt2


print best("ACAGU")
# print best("AWAGU")


