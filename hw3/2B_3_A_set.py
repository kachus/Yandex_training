list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list3=list(set(list1+list2))
print((len(list1)+len(list2)) - len(list3))