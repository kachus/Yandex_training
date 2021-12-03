
numbers=list(map(int,input().split()))
dict_numbers={}
cnt=0
for i in numbers:
    dict_numbers[i]=cnt
for i in numbers:
    if i in dict_numbers:
        dict_numbers[i]+=1
    
for key in  dict_numbers.keys():
    if dict_numbers[key]<=1:
        print(key)