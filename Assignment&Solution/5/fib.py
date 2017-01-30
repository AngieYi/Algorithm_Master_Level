def fib_naive(n):   # time:O(a^n)
  if n==1 or n==2:
    return 1
  return fib_naive(n-1) + fib_naive(n-2)

def fib_memo1(n, cache = None):# DP, time: O(n); space: O(n)
  if cache is None:
    cache = {}
  if n in cache:
    return cache[n]
  if n <= 2:
    cache[n] = 1
  else:
    fib_memo1(n-1, cache) + fib_memo1(n-2, cache)
  return cache[n]

def fib_memo2(n, cache={0:1, 1:1}): # DP,time: O(n); space: O(n)
    if n in cache:
        return cache[n]
    cache[n] = fib_memo2(n-1, cache) + fib_memo2(n-2, cache)
    return cache[n]


def fib_best(n): # DP,time: O(n); space: O(1)
    a, b = 1, 1
    for _ in xrange(n):
        a, b = b, a+b
    return b


import time
if __name__ == "__main__":
  #print fib2(2)
  #print fib2(3)
  #print fib2(4)
  for n in xrange(1,100):
    t = time.time()
    f = fib2(n)
    #f = fib(n)
    print n,time.time()-t
 