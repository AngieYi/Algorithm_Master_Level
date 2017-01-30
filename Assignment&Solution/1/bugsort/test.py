from qsort import *

# test sorted
tree = sort([4,2,6,3,5,7,1,9])
print tree

sorted_tree = sorted(tree)  # 9 is the only right child
print sorted_tree

tree = sort([4,2,6,3,5,7,1,6.5]) # 6.5 is the only left child
print tree

sorted_tree = sorted(tree)
print sorted_tree


'''
# test search0
print search0(tree,3)
x = search0(tree,0)
y = search0(tree,6.5)
print x
print y
print x is y
print x == y

print search0(tree,4)
print search0(tree,6)


# test search and insert
print search(tree,6)
print search(tree,6.5)

print insert(tree,6.5)
tree = insert(tree,6.5)
print insert(tree,3)
'''