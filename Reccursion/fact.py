def paramfib(n,ans):
    if n<1:
        print(ans)
        return 
    paramfib(n-1,ans*n)

def funfib(n):
    if n<1:
        return 1
    return funfib(n-1)*n

print(paramfib(5,1))
print(funfib(5))