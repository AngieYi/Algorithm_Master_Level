def max_wis3(a): # O(1)-space, O(n) time; with binary number for back
    x, y = 0, 0
    back = 0
    n = len(a)
    for i in range(n):
        x, y = y, max(y, x+a[i])
        temp = (x==y)
        back = back * 2 + temp      # back = back << 1 | temp
    return y, solution3(n-1, a, back)

def solution3(i, a, back):
    if i < 0:
        return []
    if (back & 1):
        return solution3(i-1, a, back >> 1)
    else:
        l_temp = solution3(i-2, a, back >> 2)
        final = l_temp + [a[i]]
        return final                # or back%2; note back>>2!

print max_wis3([7,8,5,2])