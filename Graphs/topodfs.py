def topo(adj,s,st,visited):
    visited[s] = True
    for u in adj[s]:
        if visited[u] == False:
            topo(adj,u,st,visited)

    st.append(s)

    


adj = [[],[],[3],[1],[0,1],[0,2]]
st = []
visited = [False]*len(adj)
for s in range(len(adj)):
    if visited[s] == False:
        topo(adj,s,st,visited)
    




while(st):
    print(st.pop())