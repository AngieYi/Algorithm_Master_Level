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
I use cache in max_wis(list) similar to fib2, I set the key of the cache to a tuple,
the key of the cache is the input of max_wis (need to convert list to tuple,
since the keys of a dictionary must be of an immutable data type such as strings, numbers, or tuples,
but list is mutable), the value of the cache is output of max_wis. In my implementation,
for example max_wis(7,8,5),

recursive call from top to bottom, the cache value return from bottom to top,
in this example, max_wis(7) was called two times, the second time cache was used.

max_wis(7,8,5)   cache={ (7):(7,[7]), (7,8,5):(12,[7,5]), ():(0,[]), (7,8):(8,[8]) }
max_wis(7,8)     cache={ (7):(7,[7]), ():(0,[]), (7,8):(8,[8]) }
max_wis(7)      cache={ (7):(7,[7]) }
if there is any problem, feel free to contact me!

--Hongyan (Angie) Yi

'''
def max_wis(a,cache = None):
    if cache is None:
        cache = {}
    a_t = tuple(a)
    if a_t in cache:
        return cache[a_t]
    if len(a) == 0:
        cache[a_t] = (0,[])                         # save the special case
    elif len(a) == 1:
        cache[a_t] = max((a[0],a),(0,[]))
    else:
        exclude_n = max_wis(a[:-1],cache)           # if exclude a[-1],equal to recursive max_pre
        max_prev_prev = max_wis(a[:-2],cache)
        temp_sum = max_prev_prev[0] + a[-1]
        temp_list = list(max_prev_prev[1])
        temp_list.append(a[-1])
        include_n =(temp_sum,temp_list)             # if include a[-1],should consider the max_pre_prev
        cache[a_t] = max(exclude_n,include_n)
    return cache[a_t]

import time
if __name__ == '__main__':
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

    print max_wis([7,4,-5,2])
    print max_wis2([7,4,-5,2])

    '''
    tmp_list = []
    for x in xrange(1,998):
        tmp_list.append(x)
        t = time.time()
        max_wis(tmp_list)
        print len(tmp_list),time.time()-t
    '''

