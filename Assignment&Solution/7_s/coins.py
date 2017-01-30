from collections import defaultdict
def best(X, V):
    dp = defaultdict(lambda : defaultdict(lambda: 100000000))
    back = defaultdict(lambda : defaultdict(lambda: None))
    l = len(V)
    for m in xrange(l+1):
        dp[0][m] = 0
    for i in xrange(l):
        for u in xrange(V[i]):
            dp[u][i+1], back[u][i+1] = dp[u][i], (u,i)
            used = False
            while u+V[i] <= X:
                dp[u+V[i]][i+1], _, used, back[u+V[i]][i+1] = min(
                    (dp[u][i+1] if used else dp[u][i+1]+1, 3 if used else 0, True, (u,i+1)),
                    (dp[u][i]+1, 1, True, (u,i)),
                    (dp[u+V[i]][i], 2, False, (u+V[i],i)),
                )
                u += V[i]
    if dp[X][l] == 100000000:
        return None
    pick,i,j = [0]*l,X,l
    while back[i][j] is not None:
        if i > back[i][j][0]:
            pick[j-1] += 1
        i,j = back[i][j]

    return dp[X][l], pick

if __name__ == "__main__":
    print best(47, [6, 10, 15])
    print best(59, [6, 10, 15])
    print best(37, [4, 6, 15])
    print best(27, [4, 6, 15])
    print best(75, [4, 6, 15])
    print best(17, [2, 4, 6])
