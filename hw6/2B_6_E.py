n, k = map(int, input().split())
dots = list(map(int, input().split()))
dots.sort()
left = 0
right = dots[-1] - dots[0] #max length
while left < right:
    l = (left + right) // 2
    cnt = 0
    maxright =  dots[0] - 1
    for nowx in dots:
        if nowx > maxright:
            cnt += 1
            maxright = nowx + l
    if cnt <= k:
        right = l
    else:
        left = l + 1
print(left)
 sorted (lst, key = lambda x: int(x[2:]))



