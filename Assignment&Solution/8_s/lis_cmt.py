'''
Longest (Strictly) Increasing Subsequence
input/output are lower-case strings:
lis("aebbcg")----"abcg"
lis("zyx")----"z"
tiebreaking: arbitrary. any optimal solution is ok.
'''

def lis(a):
    if len(a)<=1:
        return a
    back={-1:[0,-1]}
    for i in xrange(len(a)):
        for j in xrange(-1,i):
            if j == -1 or a[j] < a[i]:
                back[i] = max([(back[j][0]+1,j)])
    return backtrack(a,back)

def backtrack(a,back):
    length, pre = max([(back[j][0],j) for j in back])
    out = []
    for i in xrange(length):
        out.append(a[pre])
        _, new_pre = back[pre]
        pre = new_pre
    out.reverse()
    return "".join(out)

print lis("aebbcg")
# print lis("zyx")
# print lis("aebbdgc")
# print lis("bbabcd")
# print lis("aabbaa")
# print lis("aaa")
# print lis("56234199895")
# print lis("efcdab")
# print lis("56781234")