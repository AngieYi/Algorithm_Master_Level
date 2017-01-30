from random import randint
def qselect(k, a):
    if a == [] or k < 1 or k > len(a):
        return None
    else:
        pindex = randint(0, len(a)-1)
        a[0],a[pindex] = a[pindex],a[0] # change the first element with pivot
        
        # the rest part is the same as qsort
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        
        lleft = len(left)
        if k == lleft+1:
            return pivot
        elif k <= lleft:
            qselect(k,left)
        else:
            qselect(k-lleft-1,right)
