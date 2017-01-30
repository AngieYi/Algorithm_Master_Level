def solution(opt,w,index,final):
    final[index] = opt[w][index][4]
    left_w = opt[w][index][1]
    pre_i = opt[w][index][2]
    if left_w > 0 and pre_i >= 0:
        solution(opt,left_w,pre_i,final)
    return final

def best(bagWeight,item_list):
    w,types = bagWeight,len(item_list)  # first initialize the outer list with lists before adding items; Python called "list comprehension".
    opt = [[-1 for y in range(types)] for x in xrange(w+1)] # by default all the value are -1
    i = types - 1          # i is the index of last item
    j = item_list[i][2]    # j is the max amount of item i
    final_list = []
    final = {}
    for y in range(types):
        opt[0][y] = (0,)

    def top_down(w,i,j):
        if i < 0:
            return 0
        if opt[w][i] != -1:     # this is used to backtrack
            return opt[w][i][0]
        candidates = []
        for c in xrange(j+1):
            left_w = w - item_list[i][0]*c
            if left_w < 0:
                break
            else:
                value = top_down(left_w,i-1,item_list[i-1][2]) + item_list[i][1]*c
                #if value != 0: # ignore this to handle too small bag
                candidates.append((value,left_w,i-1,i,c))# the more weight left to previous item the better, so put left_w on the second position
        opt[w][i] = max(candidates)
        return opt[w][i][0]

    top_down(w,i,j)
    final = solution(opt,w,i,final)

    for k in xrange(i+1):
        if k in final:
            final_list.append(final[k])
        else:
            final_list.append(0)

    return opt[w][i][0],final_list


if __name__ == '__main__':
    print best(1, [(2, 4, 2), (3, 5, 3)])   # bag is too small,not item could put into it
    print best(2, [(3, 4, 2), (4, 5, 3)])   # bag is too small,not item could put into it
    print best(7, [(2, 5, 2), (3, 8, 2)])   # greedy not useful since [2,1] is better than [0,2]
    print best(4, [(2, 4, 2), (3, 5, 3)])   # only take first

    # test case from bounded
    print best(3, [(2, 4, 2), (3, 5, 3)])   # only take second
    print best(3, [(1, 5, 2), (1, 5, 3)])   # *reverse* lexicographical
    print best(3, [(1, 5, 1), (1, 5, 3)])   # *reverse* lexicographical
    print best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])
    print best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])

    # test case from unbounded
    print best(3, [(1, 5, 20), (1, 5, 30)])
    print best(3, [(1, 2, 60), (1, 5, 10)])
    print best(3, [(1, 2, 20), (2, 5, 20)])
    print best(58, [(5, 9, 2), (9, 18, 20), (6, 12, 20)])
    print best(92, [(8, 9, 1), (9, 10, 20), (10, 12, 20), (5, 6, 1)])