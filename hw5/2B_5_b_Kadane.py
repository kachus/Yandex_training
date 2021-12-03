length = int(input())
numbers = list(map(int,input().split()))
start_ind= 0
current_sum = 0
max_sum = numbers[0]
for end_ind in range(start_ind, length):
    current_sum += numbers[end_ind]
    if current_sum >= 0:
        if current_sum > max_sum:
            max_sum = current_sum
    elif current_sum < 0:
        current_sum = 0
        start_ind = end_ind + 1
print(max_sum)
