def checkisge(num):
    return num >= trees
def count(num):
    days_off_first = num // daysoff1 #количество выходных у каждого дровосека
    days_off_second = num // daysoff2
    current_trees = (num - days_off_first)* wcutter1 + (num - days_off_second) * wcutter2
    return current_trees

def binsearch(l,r,check):
    while l<r:
        m = (l + r)//2
        current_tress = count(m)
        if check(current_tress):
            r = m
        else:
            l = m + 1
    return l

wcutter1, daysoff1, wcutter2,daysoff2, trees = map(int, input().split())
max_days = 2*trees//(wcutter1 + wcutter2)

ans = binsearch(1, max_days, checkisge)
print(ans)
