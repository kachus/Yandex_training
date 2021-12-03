wrdcnt = {}
with open('input.txt','r') as fin:
    for line in fin:
        words = line.split()
        for word in words:
            wrdcnt[word] = wrdcnt.get(word, 0) + 1
ans=[]
for word in wrdcnt:
    ans.append((-wrdcnt[word], word))
ans.sort()
for cnt, word in ans:
    print(word)