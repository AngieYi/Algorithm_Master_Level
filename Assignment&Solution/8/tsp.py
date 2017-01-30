'''
did not finish
'''
from collections import defaultdict

def tsp(graph,end):
    opt = defaultdict(int)

    def _tsp(graph,end,opt):
        if len(graph) == 1:
            return (0,0)
        if end in opt:
            return opt[end]
        candidates = []
        for pre in graph[end]:
            tmp = graph.copy()
            del tmp[end]
            tmp_in = tmp[pre].copy()
            del tmp_in[end]
            tmp[pre] = tmp_in
            candidates.append((_tsp(tmp,pre,opt)[0] + graph[end][pre],pre))
        opt[end] = min(candidates)

    _tsp(graph,end,opt)


if __name__ == "__main__":
     graph = {
              0:{1:2,4:7},
              1:{0:2,2:3,4:6},
              2:{1:3,4:1},
              4:{0:7,1:6,2:1}
            }

     graph1 = {
              0:{1:2,4:7},
              1:{0:2,2:3,4:6},
              2:{1:3,3:5,4:1},
              3:{2:5,4:4},
              4:{0:7,1:6,2:1,3:4}
            }
     print tsp(graph,0)
     print tsp(graph,1)
     print tsp(graph,2)