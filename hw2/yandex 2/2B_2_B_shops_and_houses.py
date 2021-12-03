seq=list(map(int, input().split()))
houses=[]
shops=[]
for x in range(10):
    if seq[x]==1:
        houses.append(x)
    if seq[x]==2:
        shops.append(x)
dist=[]
dist_final=[]
i=0
for house in houses:
    for i in range(len(shops)):
        distance = abs(house-shops[i])
        dist.append(distance)
    dist_final.append(min(dist))
    dist=[]
print(max(dist_final))