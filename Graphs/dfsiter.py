def dfs(adj,s):
    visited =[False]*len(adj)
    st = [s]
    while(len(st)>0):
        s = st.pop()
        if visited[s] == False:
            print(s,end=" ")
            visited[s] = True
        
        for u in adj[s]:
            if visited[u] == False:        
                st.append(u)

dfs([[1,2],[0,3,4],[0,3],[1,2,4],[1,3]],0)
