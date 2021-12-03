#FAILED AT 15 TEST - TL EXCEEDED 
M = int(input())
segments_set = set()
seg = tuple(map(int, input().split()))
segments_set.add(seg) #wrong format, unhashable type 
while seg != tuple([0, 0]):
    seg = tuple(list(map(int, input().split())))
    if seg != tuple([0, 0])and seg[0]< M and seg[1] > 0:
        segments_set.add(seg)
segments_set= list(segments_set)
segments_set.sort()
segments = []
for i in range(len(segments_set)):
    segments.append(list(segments_set[i]))

cnt = 0
previous_right = 0
max_right = -1
good_segments = []
list_best = []
found = False
current_i = 0
great_right = -1
best_segment = []


while found == False:
    for i in range(current_i,len(segments)):
        left = segments[i][0]
        right = segments[i][1]
        if left <= previous_right and right > previous_right:
            if right > great_right:
                best_segment = segments[i] + [i]
                great_right = segments[i][1]
    if max_right < M and i == len(segments):
        found = True
        print('No solution')
    elif len(best_segment) == 0 and i < len(segments):
        found = True 
        print('No solution')
    elif len(best_segment) > 0:
        max_right = best_segment[1]
        cnt += 1
        list_best.append((best_segment))
        current_i = best_segment[2] + 1
        if max_right >= M:
            found = True
            print(cnt)
            for i in range(len(list_best)):
                print(*list_best[i][0:2])
            break
        else:
            previous_right = best_segment[1]
            best_segment = []


