def f(x):
    return a*x**3 + b*x**2 +c* x + d
def sign(num):
    return -1 if f(num)<=0 else 1

def binsearch(l,r):
    while l + eps <r:
        mid = (l + r)/2
        if sign(mid) == sign(l):
            l = mid
        else:
            r = mid
    return l

a,b,c,d = map(int,input().split())
inf = 2000
l,r = -inf, inf
eps = 0.0000001
print(binsearch(l,r))

