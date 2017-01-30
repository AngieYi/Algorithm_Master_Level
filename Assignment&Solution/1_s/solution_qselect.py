from random import randint
def qselect(k, a):
    if a == [] or k < 1 or k > len(a):
        return None
    else:
        pindex = randint(0, len(a)-1)
        a[0],a[pindex] = a[pindex],a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        lleft = len(left)
        return pivot if k == lleft+1 else \
            qselect(k, left) if k <= lleft else \
            qselect(k-lleft-1, right)

print qselect(2, [3, 10, 4, 7, 19])
print qselect(4, [11, 2, 8, 3])