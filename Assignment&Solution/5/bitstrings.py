# f(n) = 2^(n-2)+f(n-2)+f(n-1)
def num_yes(n):
    if n < 1:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1
    return pow(2,n-2)+num_yes(n-2)+num_yes(n-1)

def num_no(n):
    if n < 1:
        return None
    else:
        return pow(2,n) - num_yes(n)

if __name__ == '__main__':
    print "num_yes(0) = ",num_yes(0)
    print "num_no(0) = ",num_no(0)
    print "num_yes(1) = ",num_yes(1)
    print "num_no(1) = ",num_no(1)
    print "num_yes(2) = ",num_yes(2)
    print "num_no(2) = ",num_no(2)
    print "num_yes(3) = ",num_yes(3)
    print "num_no(3) = ",num_no(3)
    print "num_yes(4) = ",num_yes(4)
    print "num_no(4) = ",num_no(4)
    print "num_yes(5) = ",num_yes(5)
    print "num_no(5) = ",num_no(5)



