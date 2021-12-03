inf = list(map(int,input().split()))
numbers = list(map(int,input().split()))
length = inf[0]
requests = inf[1]
prefix_sum = [0]*(length+1)
for i in range(1, len(numbers) + 1):
	prefix_sum[i] = prefix_sum[i-1] + numbers[i-1]
for request in range(requests):
	borders = input().split()
	left =int(borders[0])-1
	right = int(borders[1])-1
	print(prefix_sum[right+1] - prefix_sum[left])

