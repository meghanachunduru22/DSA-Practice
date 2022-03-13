s = "abc"
n = len(s)
for i in range(1<<n):
    sb = ""
    for j in range(n):
        if i&(1<<j):
            sb = sb+s[j]
    print(sb)