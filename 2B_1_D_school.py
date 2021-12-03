num=int(input())
houses=input().split()
for h in range (num):
    houses[h]=int(houses[h])
def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None #медиана выборки
print(round(median(houses)))