parties={}
votes = 0
with open('input.txt','r') as inf:
    for line in inf:
        words = line.split()
        cnt = int(words[-1]) 
        party_name = ' '.join(words[:-1]) 
        parties[party_name] = [cnt]
        votes += cnt
f = votes / 450
free = 450
dict_sort={}
for party in parties:
    cnt = int(parties[party][0])
    parties[party].append(cnt//f)
    free -= int(cnt//f)
    dict_sort[party] = cnt%f
dict_sort=sorted(dict_sort.items(), key = lambda x: x[1], reverse=True)
for i in range(free):
    party_name = dict_sort[i][0]
    parties[party_name][1]+= 1
for party in parties:
    print(party, int(parties[party][1]))