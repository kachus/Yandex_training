L, num=input().split()
L=int(L)
num=int(num)
benches=list(map(int,input().split()))
med=L//2

n,m=0,0
ans=[]

if L%2==0:
    for i in range (0,med):
        if med+i in benches and n==0:
            ans.append(med+i)
            n=1
        if med-i-1 in benches and m==0:
            ans.append(med-1-i)
            m=1
if L%2==1:
    if med in benches:
        ans.append(med)
    else:
        for i in range (1,med+1):
            if med+i in benches and n==0:
                ans.append(med+i)
                n=1
            if med-i in benches and m==0:
                ans.append(med-i)
                m=1
print(*sorted(ans))
        