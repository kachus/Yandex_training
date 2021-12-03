def linbinsearch(l,r,check,params):
    while l < r:
        m = (l + r) // 2
        if check(m, params):
            r = m
        else:
            l = m + 1
    if l == len(seq):
        return l - 1
    return l
def checkisge(index, params):
    seq, x = params
    return seq[index] >= x
def checkisgt(index, params):
    seq, x = params
    return seq[index] > x
def findfirst(seq,x,check):
    ans = linbinsearch(0, len(seq), check, (seq, x))
    if not check(ans, (seq,x)):
        return len(seq)
    return ans

def count(seq,left_value,right_value):
    indexgt = findfirst(seq, right_value, checkisgt)
    indexge = findfirst(seq, left_value, checkisge)
    return indexgt - indexge


length = int(input())
seq = list(map(int,input().split()))
seq.sort()
request_num = int(input())
answers = []
for i in range(request_num):
    values = list(map(int,input().split()))
    left_value = values[0]
    right_value = values[1]
    answers.append(count(seq,left_value,right_value))
print(*answers)
