def fibo_iter(n):
    a, b=0, 1
    for i in range(n):
        a, b=b, a+b
    return a


def fibo_rec(n):
    if n==0 or n==1:
        return n
    return fibo_rec(n-1)+fibo_rec(n-2)


n=10
cache=[None]*(n+1)

def fibo_dynamic(n):
    if n==0 or n==1:
        return n
    if cache[n]!=None:
        return cache[n]
    cache[n]=fibo_dynamic(n-1)+fibo_dynamic(n-2)
    return cache[n]


# coin problem