import heapq
import time

def hpush(a):
    heap1 = []
    start_time = time.time()
    for item in a:
        heapq.heappush(heap1,item) # cost O(nlogn)
    end_time = time.time()
    return end_time - start_time

def hfy(a):
    start_time = time.time()
    heapq.heapify(a)               # cost O(n)
    end_time = time.time()
    return end_time - start_time

if __name__ == '__main__':
    print "--- range(0,102400,1) sorted ---"
    print "heappush",hpush(range(0,102400,1))
    print "heapify ",hfy(range(0,102400,1))
    print "--- range(102400,0,-1) reversely-sorted ---"
    print "heappush",hpush(range(102400,0,-1))
    print "heapify ",hfy(range(102400,0,-1))
