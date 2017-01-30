# get the depth of a binary tree
def depth(tree):
    ldept,rdept = 0,0
    if tree == [] or (tree[0]==[] and tree[2]==[]): # empty tree or only one node, heigth = 0
        return 0
    if tree[0] != []:
        ldept = depth(tree[0])
    if tree[1] != []:
        rdept = depth(tree[2])
    dept = max(ldept+1,rdept+1)
    return dept

# Length of the longest path in a binary tree (number of edges).
def longest(tree):
    llen, rlen, lrootlen, rootrlen, lrootrlen= 0,0,0,0,0
    if tree == [] or (tree[0] == [] and tree[2] == []):         # empty tree or only one node
        return 0
    if tree[0] != []:
        llen = longest(tree[0])
    if tree[2] != []:
        rlen = longest(tree[2])
    if tree[0] != [] and tree[2] == []:  # only has left child
        ldepth = depth(tree[0])
        lrootlen = ldepth + 1
    if tree[0] == [] and tree[2] != []:  # only has right child
        rdepth = depth(tree[2])
        rootrlen = 1 + rdepth
    if tree[0] != [] and tree[2] != []:  # has both left and right child
        ldepth = depth(tree[0])
        rdepth = depth(tree[2])
        lrootrlen = ldepth+ 2 + rdepth
    max_value = max(llen,rlen,lrootlen,rootrlen,lrootrlen)
    return max_value