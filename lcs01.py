def longestCommonSum(arr1, arr2, n):
    maxx = 0
    diff = [-1]*(2*n+1)
    pref1 = 0
    pref2 = 0   
    for i in range(n):
        pref1 += arr1[i]
        pref2 += arr2[i]
        curdif = pref1-pref2
        if diff[n+curdif] == -1:
            maxx = i+1
            diff[n+curdif] = i
        else :
            maxx = max(i-diff[n+curdif],maxx)
    return maxx


arr1 = [0, 1, 0, 1, 1, 1, 1]
arr2 = [1, 1, 1, 1, 1, 0, 1]
n = len(arr1)
print(longestCommonSum(arr1, arr2, n))