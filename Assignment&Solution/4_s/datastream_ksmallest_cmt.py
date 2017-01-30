#!/usr/bin/python
'''
   Find the k smallest numbers in a data stream of length n (k<<n),
   using only O(k) space (the stream itself might be too big to fit in memory).

   ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])
   [2, 3, 5, 7]
   ksmallest(3, xrange(1000000, 0, -1))
   [1, 2, 3]

   Note:
   a) it should work with both lists and lazy lists
   b) the output list should be sorted

'''
import random
random.seed(10)
import heapq

def ksmallest(k,l):
    heap=[]
    for x in l:
        if len(heap) < k:
            heapq.heappush(heap,-x)
        elif -x > heap[0]:              # negative could directly use -x, heap could be visited with index
            heapq.heapreplace(heap,-x)  # heapreplace replaces heap[0] with the element
    tmp = sorted([-y for y in heap])
    return tmp

    
if __name__=="__main__":
    #print ksmallest(3, [-2, 2, 9,10])
    print ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]) #[2, 3, 5, 7]

    # print ksmallest(3, [10, 2, 9, 3, 7, 8, 11, 5, 7])
    # print ksmallest(3, xrange(1000000, 0, -1))
    #
    # l = [random.randint(0,100) for r in xrange(200)]
    # print ksmallest(6,l)
    # l.sort()
    # print l