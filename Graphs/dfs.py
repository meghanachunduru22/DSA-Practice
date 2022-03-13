def dfs(adj,s,visited):
    visited[s] = True
    print(s,end=" ")
    for u in adj[s]:
        if visited[u] == False:
            dfs(adj,u,visited)
def dfsdriver(adj,s):
    visited = [False for i in range(len(adj))]
    dfs(adj,s,visited)

dfsdriver([[1,2],[0,3,4],[0,3],[1,2,4],[1,3]],0)
