def dfs(adj,s,visited):
    visited[s] = True
    # print(s,end=" ")
    for u in adj[s]:
        if visited[u] == False:
            dfs(adj,u,visited)
def dfsdrivercomp(adj):
    visited = [False for i in range(len(adj))]
    comp = 0
    for s in range(len(adj)):
        if visited[s] == False:
            comp+=1
            dfs(adj,s,visited)
    return comp

print(dfsdrivercomp([[1,2],[0,2],[0,1],[4],[3]]))