import heapq

def nsmallest(A):
    result = []
    n = len(A)
    h, ifused = [], set()
    for x in xrange(n):
        heapq.heappush(h,(A[x][0][0],x,0,0))
    while len(result) < n:
        v,x,i,j = heapq.heappop(h)
        result.append(v)
        if i+1<n and (x,i+1,j) not in ifused:
            heapq.heappush(h, (A[x][i+1][j],x,i+1,j))
            ifused.add((x,i+1,j))
        if j+1<n and (x,i,j+1) not in ifused:
            heapq.heappush(h, (A[x][i][j+1],x,i,j+1))
            ifused.add((x,i,j+1))
    return result

if __name__=="__main__":
    print nsmallest({0:[[1,2,5],[3,4,9],[6,7,8]],1:[[11,12,15],[13,14,19],[16,17,18]],2:[[21,22,25],[23,24,29],[26,27,28]]})
