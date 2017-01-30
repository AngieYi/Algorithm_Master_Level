def bsts(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    sum = 0
    if n%2 == 0:    # if n is even
        for x in xrange(n-1,n/2-1,-1):
            sum = sum + bsts(x) * bsts(n-1-x)
        return 2 * sum
    else:           # if n is odd
        for x in xrange(n-1,(n-1)/2,-1):
            sum = sum + bsts(x) * bsts(n-1-x)
        return 2 * sum + pow(bsts((n-1)/2),2)

if __name__ == '__main__':
    str1 = ""
    for x in xrange(1,15,1):
        str1 = str1 + str(bsts(x))+","
    print str1

    print "bsts(0) = ",bsts(0)
    print "bsts(1) = ",bsts(1)
    print "bsts(2) = ",bsts(2)
    print "bsts(3) = ",bsts(3)
    print "bsts(4) = ",bsts(4)
    print "bsts(5) = ",bsts(5)

