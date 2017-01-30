'''
5. find a value in a BST t, that is closest to a query x
t = [[[],2,[]],4,[[[],5,[]],6,[[],7,[]]]]
   4
  / \
 2   6        find(t,4.7) return 5.
    / \       find(t,4.1) return 4.
	5  7
'''
def find(t,x,best=None):    # best always record the current closest value
    if t == []:
        return best         # best case
    left,root,right = t     # good way to split the tree
    if best == None or abs(root-x) < abs(best-x): # compare best with root
        best = root         # at the beginning set root to best
    if x < root:
        return find(left,x,best)    # only search the left tree
    return find(right,x,best)       # only search the right tree


t = [[[],2,[]],4,[[[],5,[]],6,[[],7,[]]]]
t = []
print find(t,4.7)