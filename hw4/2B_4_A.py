colours={}
for i in range(int(input())):
    key,value=input().split()
    key=int(key)
    value=int(value)
    if key not in colours:
        colours[key]=[value]
    else:
        colours[key].append(value)
s=0
dict_ans={}
for key in colours.keys():
    for i in range(len(colours[key])):
        element=colours[key][i]
        s+=element
    dict_ans[key]=s
    s=0
list_keys=list(dict_ans.keys())
list_keys.sort()

for i in list_keys:
    print(i, dict_ans[i])