def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


if __name__ == "__main__":
     graph = {'A': ['B', 'C'],
              'B': ['C', 'D'],
              'C': ['D'],
              'D': ['C'],
              'E': ['F'],
              'F': ['C']}

     graph1 = {0:[1,4],
              1:[2,4],
              2:[3,4],
              3:[4,2],
              4:[0,1,2,3]}
     print find_shortest_path(graph,'A','D')