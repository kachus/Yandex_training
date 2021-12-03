S = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
def makedict(list):
    dict_index = {}
    for i in range(0,list[0]):
        if list[i+1] not in dict_index:
            dict_index[list[i+1]] = i
    return dict_index
dict = makedict(C)

answer = -1
found = False

for i in range(A[0]):
    if found == True:
        break
    ai = A[i+1]
    for j in range(B[0]):
        bj = B[j+1]
        C = S - (ai + bj)
        if C>=0 and found != True:
            if C in dict:
                answer = str(i)+' '+str( j)+ ' '+str(dict[C])
                found = True
                break



print(answer)
