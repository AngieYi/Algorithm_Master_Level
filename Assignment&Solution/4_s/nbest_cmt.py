## hw1 qselect with key
'''
1. (taken from my first paper: see "Algorithm 1" in Huang and Chiang (2005).)

Given two lists A and B, each with n integers, return
a sorted list C that contains the smallest n elements from AxB:
     AxB = { (x, y) | x in A, y in B }
   i.e., AxB is the Cartesian Product of A and B.
   ordering:  (x,y) < (x',y')  iff. x+y < x'+y' or (x+y==x'+y' and y<y')

You need to implement three algorithms and compare:
(a) enumerate all n^2 pairs, sort, and take top n.
enumerate the pairs cost (n^2), sort cost (n^2 logn^2), take top n cost (n), so the final result is
(n^2)+ (n^2 logn^2)+ (n) = O(n^2 logn)

(b) enumerate all n^2 pairs, but use qselect from hw1.
enumerate the pairs cost (n^2), use qselect cost (n^2), to sum up O(n^2)

(c) Dijkstra-style best-first, only enumerate O(n) (at most 2n) pairs.
first sort these two lists, then use heapq, choose a0b0 as the basic element, then push two pair of elements into the heap, a0b1 and a1b0, and then pop, each time pop one smallest until get n.
so each time pop cost (logn), 2 push cost (2logn), then n times
n*(logn + 2logn) = O(nlogn)

Hint: you can use Python's heapq module for priority queue.

'''
from random import randint
def qselect(k, a, key = lambda x:x):
    if a == [] or k < 1 or k > len(a):
        return None
    else:
        pindex = randint(0, len(a)-1)
        a[0],a[pindex] = a[pindex],a[0]
        pivot = a[0]
        left = [x for x in a if key(x) < key(pivot)]
        right = [x for x in a[1:] if key(x) >= key(pivot)]
        lleft = len(left)
        return pivot if k == lleft+1 else \
            qselect(k, left,key) if k <= lleft else \
            qselect(k-lleft-1, right,key)
## end
import heapq
mykey = lambda x: (x[0]+x[1], x[1])

# def nbesta(a, b):
#     c = [(x,y) for x in a for y in b]
#     c.sort(key = mykey)
#     return c[:len(a)]
#
# def nbestb(a, b):
#     c = [(x,y) for x in a for y in b]
#     result = [qselect(i,list(c),mykey) for i in xrange(1, len(a)+1)]
#     return result

def nbestc(a, b):
    if len(a) == []:
        return []
    sa, sb = sorted(a), sorted(b)
    l, result = len(a), []
    h, ifused = [], set()

    heapq.heappush(h, (mykey((sa[0],sb[0])), (0,0)))
    while len(result) < l:
        i,j = heapq.heappop(h)[1]
        result.append((sa[i],sb[j]))# list to store the result
        if i+1<l and (i+1,j) not in ifused:
            heapq.heappush(h, (mykey((sa[i+1],sb[j])), (i+1,j))) # heap to store the candidates
            ifused.add((i+1,j)) # set to store used index
        if j+1<l and (i,j+1) not in ifused:
            heapq.heappush(h, (mykey((sa[i],sb[j+1])), (i,j+1)))
            ifused.add((i,j+1))
    return result

if __name__ == "__main__":
    a,b = [4,1,5,3],[2,6,3,4]
    # print nbesta(a,b)
    # print nbestb(a,b)
    print nbestc(a,b)
