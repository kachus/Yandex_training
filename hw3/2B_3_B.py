numbers=list(map(int,input().split()))
dict_numbers={}
keys=set(numbers)
for i in keys:
    dict_numbers[i]=False
    
for j in numbers:
    if dict_numbers[j]==False:
        print('NO')
        dict_numbers[j]=True
    elif dict_numbers[j]==True:
        print('YES')
        