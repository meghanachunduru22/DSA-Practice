def findMedian(A):
    low = 1
    high = int(1e9)
    n = len(A)
    m = len(A[0])
    print((n+m)//2)
    while low <= high:
        mid = (low+high)>>1
        cnt = 0
        for i in range(n):
            x = countsmall(A[i],mid)
            cnt += x
            # print(A[i],mid,x)
        print(low,high,mid,cnt)
        if cnt <= (n*m)//2:
            low = mid+1
        else:
            high = mid-1
    return low

def countsmall(row,mid):
	l=0
	h=len(row)-1
	while(l<=h):
		md = (l+h)//2
		if row[md] <= mid:
			l = md+1
		else:
			h = md -1
	return l

print(findMedian([[1,3,5],[2,6,9],[3,6,9]]))