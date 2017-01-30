__author__ = "liang huang"

'''
{
	for Do until we popped all vertices:
	1) v <- pop-min       # Current target(pop the vertices with shortest path in current state)
	2) for (v, u) in E:   # E: graph,
						    # (v, u): edge between vertices v and u,
                          # this step is for all u's that linked with v we popped above
     update: (d(u), d(v) + c(v, u))      # update the path length of all vertices that linked with v
}

'''

from heapdict import heapdict
from collections import defaultdict

def shortest(n, _edges):
    edges = defaultdict(list)
    for (u, v, cost) in _edges:
        edges[u].append((v, cost))
        edges[v].append((u, cost))
    hp_dic = heapdict()
    hp_dic[0] = 0                        # alternatively, you can also set everything else to +inf
    back = {}
    popped_visited = set()                  # those already popped (i.e., black nodes)
    while len(hp_dic) > 0:
        v, distance = hp_dic.popitem()   # pop the vertex with shortest distance
        popped_visited.add(v)               # add it to visited set, (black)
        if v == n-1:                     # the current vertex is the target(fixed)
            return distance, solution(v, back)
        for (u, cost) in edges[v]:
            if u not in popped_visited:    # u is not black, not visited yet
                newd = distance + cost
                if u not in hp_dic or newd < hp_dic[u]: # white forward update;
                    hp_dic[u] = newd     # automatic decrease-key(),u is gray now
                    back[u] = v 
    return None                         # target is not reachable

def solution(v, back):
    if v == 0:
        return [0]
    return solution(back[v], back) + [v]
        
print shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])
print shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]) # unreachable