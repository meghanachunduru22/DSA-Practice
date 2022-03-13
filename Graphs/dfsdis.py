def dfs(adj,s,visited):
    visited[s] = True
    print(s,end=" ")
    for u in adj[s]:
        if visited[u] == False:
            dfs(adj,u,visited)
def dfsdriver(adj):
    visited = [False for i in range(len(adj))]
    for s in range(len(adj)):
        if visited[s] == False:
            dfs(adj,s,visited)

dfsdriver([[1,2],[0,2],[0,1],[]])
