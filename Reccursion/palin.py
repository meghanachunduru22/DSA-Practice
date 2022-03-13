s = "abccba"
n = 6
def ispalin(i):
    if i >= n//2:
        return True
    if s[i]!=s[n-i-1]:
        return False
    return ispalin(i+1)

print(ispalin(0))