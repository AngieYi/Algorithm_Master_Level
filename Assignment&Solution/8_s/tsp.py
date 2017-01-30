'''
Traveling Salesman Problem (TSP).
   Given an undirected graph of n nodes (0..n-1) representing a road network,
   the traveling salesman has to start from city 0 and visit each city once and only once,
   and return to city 0. Find the minimum-length tour (cycle) that satisifies these conditions.

graph input:
a pair: the number of nodes n, and the list of edges.
(n, [(u, v, cost), ... ])

internal graph representation: adjacency list (hash: node->list_of_neighbors)
'''

# time complexity O(2^n n^3)

from collections import defaultdict

def bottom_up(n, _edges):
    edges = defaultdict(list)
    for (u, v, cost) in _edges: # undirected
        edges[u].append((v, cost))
        edges[v].append((u, cost))

    # by default any weight between two cities is infinite
    best = defaultdict(lambda : defaultdict(lambda: float("inf")))
    # best[size][S, i]  --- organize best by size (|S|)
    best[1][frozenset([0]), 0] = 0 # frozenset is immutable,set is unhashable
    
    back = {}   # back[S, i], no need to organize by size

    for size in xrange(2, n+1):         # 2 to n
        for S, j in best[size-1]:       # all reachable (S, j) with |S|=size-1  # O(choose(n, size) * size).
            for i, cost in edges[j]:    # all possible edge j--cost-->i
                if i not in S:
                    newS = S | frozenset([i])   # expand visited set,newS is still a frozenset
                    newcost = best[size-1][S, j] + cost
                    if newcost < best[size][newS, i]:   # forward update
                        best[size][newS, i] = newcost
                        back[newS, i] = j

    full = frozenset(range(n))
    # only works for undirected graph
    # tmp = []
    # for j,cost in edges[0]:
    #     tmp.append((best[n][full, j] + cost, j))
    # goal, goalj = min(tmp)
    goal, goalj = min((best[n][full, j] + cost, j) for j, cost in edges[0])
    
    if goal < float("inf"):
        return goal, solution(back, full, goalj) + [0]
    return None

def solution(back, S, v):
    if v == 0:
        return [0]
    solution_newS =  S - frozenset([v])
    solution_newv =  back[S,v]
    final = solution(back, solution_newS, solution_newv)
    return final+[v]
    #return solution(back, S - frozenset([v]), back[S, v]) + [v]

# print bottom_up(3, [(0,1,1), (1,2,2), (2,0,3)])
# print bottom_up(3, [(0,1,1), (1,2,2)])          # impossible
print bottom_up(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,1), (1,3,6)])
# print bottom_up(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,1), (1,3,6), (3,0,1)])

#print bottom_up(5, [(0,1,2),(0,4,7),(1,2,3),(1,4,6),(2,3,5),(2,4,1),(3,4,4)])
