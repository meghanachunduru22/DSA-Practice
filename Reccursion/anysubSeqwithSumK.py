st = [1,2,1]
n = len(st)
k = 2


def sub(i,arr,s):
    if i>=n:
        if s == k:
            print(arr)
            return True
        else:
            return False
    arr.append(st[i])
    s += st[i]
    if sub(i+1,arr,s):
        return True
    arr.remove(st[i])
    s -= st[i]
    if sub(i+1,arr,s):
        return True
    return False


sub(0,[],0)