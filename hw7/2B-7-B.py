n = int(input())
events = []
max_machines = 0
m_in_service = set()
cnt = 0
for i in range(n):
    tin, tservice = map(int, input().split())
    events.append((tin, 1, i))
    events.append((tin + tservice, -1, i))
events.sort()
for i in range(len(events)):
    if events[i][1] == -1:
        m_in_service.remove(events[i][2])
        cnt -= 1
    elif events[i][1] == 1:
        m_in_service.add(events[i][2])
        cnt += 1
    if cnt > max_machines:
        max_machines = cnt
print(max_machines)
