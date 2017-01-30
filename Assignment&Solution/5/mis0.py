def max_wis2(a):
    exclusive = [(0,[])]    # base case
    inclusive = [(0,[])]    # base case
    if a == []:
        return (0, [])      # base case
    for x in a:
        exclusive.append(max(inclusive[-1],exclusive[-1])) # if exclusive n,then there is only 2 options: inclusive(n-1) or exclusive(n-1)
        temp_sum = exclusive[-2][0] + x     # if inclusive n,it will not exclusive n-1
        temp_list = list(exclusive[-2][1])  # create a copy of the list without changing it, otherwise it will change original
        temp_list.append(x)
        inclusive.append((temp_sum,temp_list))
    return max(exclusive[-1],inclusive[-1]) # there is only two choices including/excluding n

def max_wis0(a):
    length = len(a)
    if length == 0:
        return (0,[])
    exclude_n = max_wis(a[:length-1])           # if exclude a[-1],equal to recursive max_pre
    max_prev_prev = max_wis(a[:length-2])
    temp_sum = max_prev_prev[0] + a[-1]
    temp_list = list(max_prev_prev[1])
    temp_list.append(a[-1])
    include_n =(temp_sum,temp_list)             # if include a[-1],should consider the max_pre_prev
    return max(exclude_n,include_n)

def max_wis(a):
    length = len(a)
    if length == 0:
        return (0,[])
    if length == 1:
        return max((a[0],a),(0,[]))
    exclude_n = max_wis(a[:-1])           # if exclude a[-1],equal to recursive max_pre
    max_prev_prev = max_wis(a[:-2])
    temp_sum = max_prev_prev[0] + a[-1]
    temp_list = list(max_prev_prev[1])
    temp_list.append(a[-1])
    include_n =(temp_sum,temp_list)             # if include a[-1],should consider the max_pre_prev
    return max(exclude_n,include_n)

import time
if __name__ == '__main__':
    tmp_list = []
    for x in xrange(1,998):
        tmp_list.append(x)
        t = time.time()
        max_wis(tmp_list)
        print len(tmp_list),time.time()-t

    '''
    print max_wis([])
    print max_wis2([])

    print max_wis([-2])
    print max_wis2([-2])

    print max_wis([-2,-7])
    print max_wis2([-2,-7])

    print max_wis([-2,-7,8])
    print max_wis2([-2,-7,8])

    print max_wis([4])
    print max_wis2([4])

    print max_wis([7,8,5])
    print max_wis2([7,8,5])

    print max_wis([2,7,4,3,-9,8,6,5])
    print max_wis2([2,7,4,3,-9,8,6,5])

    print max_wis([2,7,4,3,-9,-8,-6,-5])
    print max_wis2([2,7,4,3,-9,-8,-6,-5])

    print max_wis([2,7,4,3,-9,-8,-6,-5,20])
    print max_wis2([2,7,4,3,-9,-8,-6,-5,20])

    print max_wis([-2,0,-7,8])
    print max_wis2([-2,0,-7,8])

    print max_wis([-1,8,10])
    print max_wis2([-1,8,10])
    '''

