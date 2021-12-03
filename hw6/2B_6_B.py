def checkisge(index, params):
    seq, x = params
    return seq[index] >= x
def checkisse(index, params):
    seq, x = params
    return seq[index] <= x
def findfirst(seq,x, dictionary):
    if x not in dictionary:
        first_index = linbinsearch(0, len(seq) - 1, checkisge, (seq,x))
        second_index = linbinsearch(0,len(seq) - 1, checkisse, (seq[::-1],x))
        if seq[first_index] != x:
            dictionary[x] = [0,0]
        else:
            dictionary[x] = [first_index + 1, abs(second_index - len(seq))]
    return dictionary[x]
        

def linbinsearch(l, r, check, checkparams):
    while l<r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l
answers = {}
length_seq = int(input())
seq = list(map(int, input().split()))
length_check = int(input())
numbers_check = list(map(int, input().split()))
for i in range(length_check):
    x = numbers_check[i]
    if seq[-1] >= x:
        print(*findfirst(seq, x, answers))
    else: 
        print(0, 0)
