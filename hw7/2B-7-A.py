n = int(input())
events = []
open_segs = set()
cnt = 0
length = 0
for i in range(n):
    open, close = map(int, input().split())
    events.append((open, -1, i)) #opening before closing
    events.append((close, 1, i))
events.sort()
start = events[0][0]
for i in range(len(events)):
    if events[i][1] == -1:
        open_segs.add(events[i][2])
        cnt += 1
    elif events [i][1] == 1:
        open_segs.remove(events[i][2])
        cnt -= 1
    if len(open_segs) == 0 and i < len(events) - 1:
        finish = events[i][0]
        length += (finish - start)
        start = events[i+1][0]
    if  i == len(events) - 1:
        length += events[i][0] - start
print(length)
