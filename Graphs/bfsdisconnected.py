adj = [[1,2],[0,3],[0,3],[1,2],[5,6],[4,6],[4,5]]
def bfs(adj,s,visited):
    q = [s]  
    visited[s] = True
    while(len(q)>0):
        cur = q.pop(0)
        print(cur,end=" ")
        for i in adj[cur]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True

def bfsdis(adj):
    visited = [False for i in range(len(adj))]
    for i in range(len(adj)):
        if visited[i] ==False:
            bfs(adj,i,visited)
    



bfsdis(adj)