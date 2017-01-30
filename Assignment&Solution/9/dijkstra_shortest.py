from collections import defaultdict
from heapq import heappush,heappop

# time:O(V+E)logE, space:O(V+E)
def solution(last,opt):
    if last == 0:
        return [0]
    return solution(opt[last][1],opt)+[last]

def shortest(num,graph):
    end_dic = defaultdict(list)
    opt = defaultdict(list)                 # [cost,start]
    for (start,end,cost) in graph:          # time O(E),space O(E)
        end_dic[end].append((start,cost))

    def _shortest(end,end_dic,opt):
        heap = []
        if end == 0:
            return (0,0)                    # weight, index
        if end in opt:
            return opt[end]
        for (start,cost) in end_dic[end]:  # time O(ElogE),space O(E)
            heappush(heap,(_shortest(start,end_dic,opt)[0]+cost,start))
        opt[end] = heappop(heap)           # time O(VlogE),space O(V)
        return opt[end]

    shortest_dis = _shortest(num-1,end_dic,opt)[0]
    return (shortest_dis,solution(num-1,opt))

print shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])
print shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,1), (1,3,6)])
print shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,1),(1,3,6),(0,4,5),(1,4,6),(3,4,3)])
