L, num=input().split()
L=int(L)
num=int(num)
benches=list(map(int,input().split()))
med=L//2

n,m=0,0
ans=[]
x=0
if L%2==0:
    i=0
    j=1
    while i<=med:
        if m==1 and n==1:
            break
        if med+i in benches and m!=1:
            ans.append(med+i)
            m=1
        if med-j in benches and n!=1:
            ans.append(med-j)
            n=1
        i+=1
        j+=1
if L%2==1:
    i=1
    if med in benches:
        ans.append(med)
    if med not in benches:
        while i<=med:
            if m==1 and n==1:
                break
            if med+i in benches and m!=1:
                ans.append(med+i)
                m=1
            if med-i in benches and n!=1:
                ans.append(med-i)
                n=1
            i+=1
ans.sort()
print(*set(ans))