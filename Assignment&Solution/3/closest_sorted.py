import bisect

def find(a,key,num):
    index = bisect.bisect(a,key)    # find the index that key is suppose to insert,cost logn

    record = []
    i = index - 1                   # use i and j two pointers to search in two direction
    j = index
    count = 0
    while((count < num) and (i >= 0 ) and (j <= len(a) - 1)):
        l_dis = abs(a[i] - key)
        r_dis = abs(a[j] - key)
        if l_dis > r_dis:
            record.append(a[j])
            j += 1
            count += 1
        elif l_dis == r_dis:        # in case two numbers are equally close to x, choose the smaller one
            record.append(a[i])     # first append smaller numbers
            i -= 1
            count += 1
            if(count < num):
                record.append(a[j]) # then if still not full, append bigger numbers
                j += 1
                count += 1
        else:
            record.append(a[i])
            i -= 1
            count += 1

    while((count < num) and (i < 0 ) and (j <= len(a) - 1)):
        record.append(a[j])
        j += 1
        count += 1

    while((count < num) and (i >= 0 ) and (j > len(a) - 1)):
        record.append(a[i])
        i -= 1
        count += 1

    record.sort()                   # since record is very short,so the sort costs O(1) time.
    return record

if __name__ == '__main__':
    print find([1,2,3,4,4,7], 5.2, 2)
    print find([1,2,3,4,4,7], 6.5, 3)
    print find([1,2,3,4,4,6,6], 5, 3)
    print find([1,2,3,4,4,5,6], 4, 5)
    print find([3,4,4,5,6],1,3)
    print find([1,2,3,4,4,5,6], 7, 2)