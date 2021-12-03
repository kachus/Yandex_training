goodplates=[]
checkplates=[]
nowcount=0
ans=[]
for num1 in range(int(input())):
    goodplates.append(input())
for num2 in range(int(input())):
    checkplates.append(input())
for i in checkplates:
    cnt=0
    for j in goodplates:
        if set(i).issuperset(set(j))==True:
            cnt+=1
    if cnt>=nowcount:
        if cnt>nowcount:
            ans=[]
            ans.append(i)
            nowcount=cnt
        elif cnt==nowcount:
            ans.append(i)
            nowcount=cnt
print(*ans,sep='\n')
