num_1=int(input())
num_list=[]
while num_1!=0:
    num_list.append(num_1)
    num_1=int(input())
cnt=0
for number in num_list:
    if number==max(num_list):
        cnt+=1
print(cnt)