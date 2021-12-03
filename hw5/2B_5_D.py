seq = input()
def goodseq(seq):
    balance = 0
    answer = 'YES'
    for i in range(len(seq)):
        if seq[i] == ')':
            balance -=1
        if seq[i]=='(':
            balance +=1
        if balance <0:
            answer = 'NO'
            break
    if balance !=0:
        answer = 'NO'
    return answer

print(goodseq(seq))
