# Name: Hongyan Yi
# ONID: yih

def num_inversions(a):  # it's the by product of merge sort
    if len(a) <= 1:
        return 0
    mid = len(a)//2
    lhalf = a[:mid]     # do not put lhalf and rhalf after recursive call
    rhalf = a[mid:]
    lnum_inverse = num_inversions(lhalf)
    rnum_inverse = num_inversions(rhalf)
    num_inverse = lnum_inverse + rnum_inverse

    i = j = k = 0
    while(i < len(lhalf) and j < len(rhalf)): # use two pointers to compare
        if lhalf[i] < rhalf[j]:
            a[k] = lhalf[i]     # save the ordered one to a[k]
            i += 1
        else:
            a[k] = rhalf[j]     # save the ordered one to a[k]
            j += 1
            num_inverse += len(lhalf)-i
        k += 1

    while(i < len(lhalf)): # consider lhalf separately, if rhalf has already done
         a[k] = lhalf[i]
         i += 1
         k += 1

    while(j < len(rhalf)): # consider rhalf separately, if lhalf has already done
         a[k] = rhalf[j]
         j += 1
         k += 1
    return num_inverse