adj = [[1,3],[0,2,3],[1,6],[0,4],[3,5],[4,6],[2,5,7,8],[6,8],[6,7]]
distance = [100000]*len(adj)
src = 0
distance[src] = 0
q = [src]
while q:
    x = q.pop(0)
    distthrx = distance[x]
    for u in adj[x]:
        if distthrx + 1 < distance[u]:
            distance[u] = distthrx + 1
            q.append(u)
print(distance)
