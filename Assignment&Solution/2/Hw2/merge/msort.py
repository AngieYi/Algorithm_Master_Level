def mergesort(a):
    alen = len(a)
    if(alen > 1):
        mid = alen // 2
        lhalf = a[:mid]     # do not put lhalf and rhalf after recursive call
        rhalf = a[mid:]
        mergesort(lhalf)
        mergesort(rhalf)
        i = j = k = 0
        while(i < len(lhalf) and j < len(rhalf)): # use two pointers to compare
            if lhalf[i] < rhalf[j]:
                a[k] = lhalf[i]     # save the ordered one to a[k]
                i += 1
            else:
                a[k] = rhalf[j]     # save the ordered one to a[k]
                j += 1
            k += 1

        while(i < len(lhalf)): # consider lhalf separately, if rhalf has already done
             a[k] = lhalf[i]
             i += 1
             k += 1

        while(j < len(rhalf)): # consider rhalf separately, if lhalf has already done
             a[k] = rhalf[j]
             j += 1
             k += 1

        
    