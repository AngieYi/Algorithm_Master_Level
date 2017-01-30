import random
def qsort_3way(a):
    if a == []: return []
    pivot = a[random.randint(0,len(a)-1)]
    left = [x for x in a if x < pivot]
    mid = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return qsort_3way(left) + mid + qsort_3way(right)

def qsort_2way_Rpivot(a):
    if a == []: return []
    pivot = a[random.randint(0,len(a)-1)]
    left = [x for x in a if x < pivot]
    right = [x for x in a if x > pivot]
    return qsort_2way_Rpivot(left) + [pivot] + qsort_2way_Rpivot(right)

def qsort_2way_0pivot(a):
    if a == []: return []
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x >= pivot]
    return qsort_2way_0pivot(left) + [pivot] + qsort_2way_0pivot(right)

print qsort_3way([7,4,5,6,8,8,9])
print qsort_2way_Rpivot([7,4,5,6,8,8,9])
print qsort_2way_0pivot([7,4,5,6,8,8,9])