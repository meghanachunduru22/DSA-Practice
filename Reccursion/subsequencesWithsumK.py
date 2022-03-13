st = [1,2,1]
n = len(st)
k = 2


def sub(i,arr,s):
    if i>=n:
        if s == k:
            print(arr)
        return
    arr.append(st[i])
    s += st[i]
    sub(i+1,arr,s)
    arr.remove(st[i])
    s -= st[i]
    sub(i+1,arr,s)

sub(0,[],0)