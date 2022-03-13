adj = [[(1,2),(4,1)],[(2,3)],[(3,6)],[],[(2,2),(5,4)],[(3,1)]]
# adj = [[],[],[(3,1)],[(1,1)],[(0,1),(1,1)],[(0,1),(2,1)]]

def dfs(adj,src,visited,topostack):
    visited[src] = True
    for u in adj[src]:
        if visited[u[0]] == False:
            dfs(adj,u[0],visited,topostack)

    topostack.append(src)


def topo(adj):
    visited = [False]*len(adj)
    topostack = []

    for s in range(len(adj)):
        if visited[s] == False:
            dfs(adj,s,visited,topostack)
    return topostack


topostack = topo(adj)

def shrtstDAG(adj,topostack,distance):
    
    while topostack:
        x = topostack.pop()
        if distance[x] != 100000:    
            for u in adj[x]:
                if distance[x] + u[1] < distance[u[0]]:
                    distance[u[0]] = distance[x] + u[1]
        # else:
    return distance

src = 0
distance = [100000]*len(adj)
distance[src] = 0
shrtstDAG(adj,topostack,distance)
print(distance)

        

