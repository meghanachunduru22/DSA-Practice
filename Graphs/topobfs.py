adj = [[],[],[3],[1],[0,1],[0,2]]
inDegree = [0]*len(adj)
q = []
for i in range(len(adj)):
    for j in adj[i]:
        inDegree[j]+=1

print(inDegree)

for i in range(len(inDegree)):
    if inDegree[i] == 0:
        q.append(i)
out = []
while(q):
    x = q.pop(0)
    out.append(x)
    for u in adj[x]:
        
        inDegree[u] -= 1
        if inDegree[u] == 0:
            q.append(u)
print(out)