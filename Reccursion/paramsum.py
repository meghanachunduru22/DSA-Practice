def summ(n,s):
    if n<1:
        print(s)
        return
    summ(n-1,s+n)
summ(5,0)
