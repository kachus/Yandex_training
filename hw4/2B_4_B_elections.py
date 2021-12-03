with open ('input.txt') as inf,open('output.txt','w') as out:
    dict={}
    for line in inf:
        line=line.strip().split()
        if line[0] not in dict:
            dict[line[0]]=[int(line[1])]
        else:
            dict[line[0]].append(int(line[1]))
    sum=0
    votes={}
    presidents=list(dict.keys())
    presidents.sort()
    for president in presidents:
        for i in range(len(dict[president])):
            sum+=dict[president][i]
        votes[president]=sum
        sum=0
    for key in votes.keys():
        out.write(str(key)+' '+str(votes[key])+'\n')