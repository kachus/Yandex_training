n, k = map(int, input().split())
dots = list(map(int, input().split()))
dots.sort()
left = 0
right = dots[-1] - dots[0]
cnt = k
def countcurrentright(x):
    maxright = dots[0] + x
    cnt = k
    for dot in dots:
        if cnt-1>0:
            if dot > maxright:
                maxright = dot + x
                cnt -=1
        else:
            break
    return maxright
while left < right:
    mid = (left + right) // 2
    current_right = countcurrentright(mid)
    if current_right >= dots[-1]:
        right = mid
    else:
        left = mid + 1
print(left)
