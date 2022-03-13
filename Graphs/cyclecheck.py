adj = [[1,2],[0,3,4],[0,3],[1,2,4],[1,3]]
visited = [False]*len(adj)

def dfs(adj,s,visited):
    st = [(s,-1)]
    while st:
        x = st.pop()[0]
        if not visited[x]:
            visited[x] = True
            print(x,end=" ")
            for u in adj[x]:
                if visited[u] == False:
                    st.append((u,x))
                else:
                    if x != u:
                        return True
    return False       

for u in range(len(adj)):
    
    if visited[u] == False:
        # print("hi")
        print(dfs(adj,u,visited))


            

