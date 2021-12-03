list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
cnt=0
for i in list1:
    if i in list2:
        cnt+=1
print(cnt)