import heapq

def mergesorted(a,k):
     # generate k elements
    k_elem = []
    sorted_k = []
    for i in range(0,len(a),k):
        k_elem.append((a[i],i))
    heapq.heapify(k_elem)
    for j in range(len(a)):
        poped_tuple = heapq.heappop(k_elem)
        sorted_k.append(poped_tuple[0])
        next_index = poped_tuple[1]+1
        heapq.heappush(k_elem,(a[next_index],next_index))
    return sorted_k

def kmergesort(a,k):
    length = len(a)
    if length <= 1:
        return a

    if length <= k:
        tmp = []
        heapq.heapify(a)
        while a:
            x = heapq.heappop(a)
            tmp.append(x)
        a = tmp
        return a

    for i in range(0,len(a),k):
        return mergesorted(kmergesort(a[i:i+k],k),k)

if __name__ == '__main__':
    final = kmergesort([4,1,5,2,6,3,7,0],3)
    print final

