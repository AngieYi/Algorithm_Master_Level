from collections import defaultdict

'''
class memoize:
    def __init__(self, func):
        self.func = func
        self.known_keys = []
        self.known_values = []

    def __call__(self, *args, **kwargs):
        key = (self.func.__name__, args, kwargs)

        if key in self.known_keys:
            i = self.known_keys.index(key)
            return self.known_values[i]
        else:
            value = self.func(*args, **kwargs)
            self.known_keys.append(key)
            self.known_values.append(value)

            return value

@memoize
def bsts_rec(n):
    if n == 0:
        return 1
    result = 0
    for l in xrange(0, n):
        result += bsts_rec(l) * bsts_rec(n-1-l)
    return result

def bsts(n):
    dp = defaultdict(int)
    dp[0] = 1
    for x in xrange(1, n+1):
        result = 0
        for y in xrange(0, x):
            result += dp[y] * dp[x-y-1]
        dp[x] = result
    return dp[n]

if __name__ == "__main__":
    for n in xrange(10):
        print bsts(n)
    # for n in xrange(10):
    #     print bsts_rec(n)

'''

def bsts(n):
    dp = defaultdict(int)
    dp[0] = 1

    def _bsts(n):
        if n == 0 or 1:
            _bsts[n] = 1
        result = 0
        for i in xrange(0, n):
            result += _bsts[i] * _bsts[n-1-i]
        dp[n] = result
        return dp[n]

    return _bsts(n)


print "bsts(0) = ",bsts(0)
print "bsts(1) = ",bsts(1)
print "bsts(2) = ",bsts(2)
print "bsts(3) = ",bsts(3)
print "bsts(4) = ",bsts(4)
print "bsts(5) = ",bsts(5)