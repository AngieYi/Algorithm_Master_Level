from collections import deque
from collections import defaultdict

# Sum: time:O(V+E),space:O(V+E)?
def order(num,graph):
    final_list = []     # final output list for order of nodes
    out_adjl = defaultdict(list)

    # time:O(E),space:O(E)
    for (start,end) in graph:
        out_adjl[start].append(end) # generate out adjacent list
        if out_adjl[end] == []:     # tricky here,not necessary, but need out_adjl[v] exist,if out_degree = 0
            out_adjl[end] = []

    # time:O(V),space:O(V)
    in_degree = { u:0 for u in out_adjl } # initial all nodes in-degree,prepare for update

    # time:O(E)
    for u in out_adjl:                      # loop each node to update in-degree
        for v in out_adjl[u]:
            if v != []:
                in_degree[v] += 1

    # time:O(2V):appendleft+pop,space:O(2V):zeroin_deq + final_list
    zeroin_deq = deque()                    # define a deque object to save all zero in-degree nodes
    for u in in_degree:
        if in_degree[u] == 0:
            zeroin_deq.appendleft(u)    # need to keep order, first come first out

    while zeroin_deq:                 # check whether it's empty to keep iteration
        u = zeroin_deq.pop()          # choose node of zero in-degree
        final_list.append(u)          # add to final list
        for v in out_adjl[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                zeroin_deq.appendleft(v)

    if len(final_list) == len(out_adjl):
        return final_list
    else:                      # if there is a cycle,
        return None            # then return an empty list

print order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
print order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
print order(4, [(0,1), (1,2), (2,1), (2,3)])
print order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,8),(3,5), (4,5), (5,6), (5,7)])


