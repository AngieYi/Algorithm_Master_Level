from collections import defaultdict
'''
not work,when I del a node from a adjacent list(dictionary),
I could not loop the new dictionary since it's updated.
as dictionary changed size during iteration.
need to consider other data structure.
'''
def order(num,graph):
    in_adl, out_adl = defaultdict(list),defaultdict(list)
    t_order = []
    # for i in xrange(num):
    #     in_adl[i],out_adl[i] = [],[]
    for (start,end) in graph:
        if in_adl[start] == []:
            in_adl[start] = []
        in_adl[end].append(start)


    for (start,end) in graph:
        out_adl[start].append(end)
    while len(in_adl)!=0:
        for key in in_adl:
            if len(in_adl[key]) == 0:
                t_order.append(key)
                del in_adl[key]
                out_li = out_adl[key]
                for x in out_li:
                    in_adl[x].remove(key)
    return t_order

if __name__ == '__main__':
    #print order(8,[(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
    print order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
    #print order(4, [(0,1), (1,2), (2,1), (2,3)])
    #print order(8, [('a','c'), ('b','c'), ('b','c'), ('b','d'), ('d','c'), ('c','e'), ('d','e'), ('e','f'), ('e','g')])


