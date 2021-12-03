num=int(input())
diplomas=list(map(int,input().split()))
diplomas.sort()
sec=0
for i in range(0,num-1):
    sec+=diplomas[i]
print(sec)