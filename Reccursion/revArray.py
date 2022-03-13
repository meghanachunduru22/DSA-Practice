a = [1,2,3,4,5]
n = 5
def rev(i):
    if i>=n//2:
        return
    a[i],a[n-i-1] = a[n-i-1],a[i]
    rev(i+1)

rev(0)
print(a)

