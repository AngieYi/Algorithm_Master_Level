
#O(n) in both time and space.
def fib1(n, cache={0:1, 1:1}):
    if n in cache:
        return cache[n]
    cache[n] = fib1(n-1, cache) + fib1(n-2, cache)
    return cache[n]


def fib2(n):
    a, b = 1, 1
    for _ in xrange(n):
        a, b = b, a+b
    return b
