from collections import deque
from collections import defaultdict


def solution(final_p,opt):
    if opt[final_p][0] == 0:        # base case: if it's current length == 0
        return [final_p]
    return solution(opt[final_p][1],opt)+[final_p]

def longest(num,graph):
    final_list = []                 # final output list for order of nodes
    out_adjl = defaultdict(list)
    opt = defaultdict(lambda:(0,-1))# current length=0, previous node is -1

    for (start,end) in graph:
        out_adjl[start].append(end) # generate out adjacent list
        if out_adjl[end] == []:     # tricky here,not necessary, but need out_adjl[v] exist,if out degree = 0
            out_adjl[end] = []

    in_degree = { u : 0 for u in out_adjl }     # initial all nodes in-degree,prepare for update
    for u in out_adjl:              # loop each node to update in-degree
        for v in out_adjl[u]:
            if v != []:
                in_degree[v] += 1

    zeroin_deq = deque()                 # define a deque object to save all zero in-degree nodes
    for u in in_degree:
        if in_degree[u] == 0:
            zeroin_deq.appendleft(u)    # need to keep order, first come first out
            opt[u] = (0,-1)

    while zeroin_deq:                 # check whether it's empty to keep iteration
        u = zeroin_deq.pop()          # choose node of zero in-degree
        final_list.append(u)          # add to final list
        for v in out_adjl[u]:
            if (opt[u][0] + 1) > opt[v][0]:
                opt[v] = (opt[u][0] + 1,u)
            in_degree[v] -= 1
            if in_degree[v] == 0:
                zeroin_deq.appendleft(v)

    final_p = final_list[-1]

    return (opt[final_p][0],solution(final_p,opt))

print longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4),(3,5), (4,5), (5,6), (5,7)])
print longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3),(3,5), (4,5), (5,6), (5,7)])
print longest(5,[(0,4),(1,4),(2,3),(3,4),(4,5)])
print longest(12, [(0,2), (1,2), (2,3), (2,4), (3,4),(3,8),(8,9),(9,10),(10,11),(3,5), (4,5), (5,6), (5,7)])
print longest(14, [(0,2),(1,2),(13,12),(12,2),(2,3), (2,4), (3,4),(3,8),(8,9),(9,10),(10,11),(3,5), (4,5), (5,6), (5,7)])
print longest(14, [(13,12),(12,2),(0,2),(1,2),(2,3), (2,4), (3,4),(3,8),(8,9),(9,10),(10,11),(3,5), (4,5), (5,6), (5,7)])
print longest(4,[(0,5),(1,5),(2,5),(3,5)])
print longest(4,[(5,0),(5,1),(5,2),(5,3)])



