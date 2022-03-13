def findNthRootOfM(n,m):
    # Write your Code here.
    return bs(n,m)
    
def bs(n,m):

    l = 1
    h = m
    ct = 0
    while((h-l)>0.00001 ):
        ct+=1
        if ct == 25:
            break
        mid = (l+h)/2.0
        mid =  float("{0:.5f}". format(mid))
        print(l,h,mid)
        
        if mid**n < m:
            print("<")
            l = mid
            
        else:
            h = mid
            
    # return  ("{0:.6f}". format(h))

    
    
# def power(x,n):
#     ans = 1
#     isnegative = (n<0)
#     if isnegative:
#         n = -n
#     while n:
#         if n%2 == 0:
#             n = n//2
#             x = x*x
#         else:
#             ans = x*ans
#             n-=1
#     if isnegative:
#         return 1/ans
#     return ans

print(findNthRootOfM(3,27))