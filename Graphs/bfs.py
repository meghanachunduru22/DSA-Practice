adj = [[1,2],[0,2,3],[0,1,3,4],[1,2,4],[2,3]]
def bfs(adj,s):
    q = [s]
    visited = [False for i in range(len(adj))]
    visited[s] = True
    while(len(q)>0):
        cur = q.pop(0)
        print(cur,end=" ")
        for i in adj[cur]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
bfs(adj,0)