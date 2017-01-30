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



'''
the max sum is right, but the elements sometimes not correct.I know that when one element used to be chosen,
but after bigger number comes, the back value should change from 1 to 0, It's time consuming to do this,
so I stop.
'''
def max_wis(a,cache = None):    #{index:(opt,back)}
    if cache is None:
        cache = {-1:(0,0)}
    index = len(a)-1
    li_temp = []
    if index in cache:
        max_sum = cache[index][0]
        while cache[index][1] == 1 and index >= 0:
            li_temp.append(a[index])
            index = index -1
        return (max_sum,li_temp)
    if index == 0:
        if a[0] > 0:
            cache[0] = (a[0],1)
            return (a[0],a)
        else:
            cache[0] = (0,0)    # if <= 0,then not use it
            return (0,[])
    else:
        exclude_n = max_wis(a[:-1],cache)           # if exclude a[-1],equal to recursive max_pre
        max_prev_prev = max_wis(a[:-2],cache)
        temp_sum = max_prev_prev[0] + a[-1]
        temp_list = list(max_prev_prev[1])          # copy of this cost time
        temp_list.append(a[-1])
        include_n =(temp_sum,temp_list)             # if include a[-1],should consider the max_pre_prev
        if include_n[0] > exclude_n[0]:
            cache[index] = (include_n[0],1)
            return include_n
        else:
            cache[index] = (exclude_n[0],0)
            return exclude_n

import time
if __name__ == '__main__':
    print max_wis([2,7,4,3,-9,8,6,5])


