s = [3,1,2]
n = len(s)

def sub(i,arr):
    if i>=n:
        print(arr)
        return
    arr.append(s[i])
    sub(i+1,arr)
    arr.remove(s[i])
    sub(i+1,arr)

sub(0,[])