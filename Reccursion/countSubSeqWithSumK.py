nums = [1,2,1]
n = len(nums)
k = 2

def count(i,s,ct):
    if i >= n:
        if s==k:
            return 1
        else:
            return 0
    
    
    s += nums[i]
    l = count(i+1,s,ct)
    s-= nums[i]
    r = count(i+1,s,ct)
    return l+r

print(count(0,0,0))


