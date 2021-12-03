numbers = [1,2,3,-3,5]
prefixsum = [0]*(len(numbers)+1)
for i in range(1,len(prefixsum)):
    prefixsum[i] = prefixsum[i-1] + numbers[i-1]
p_min = prefixsum[0]
maximums = []
for right in range(1,len(numbers)):
    for left in range(1,right):
        if prefixsum[left]<p_min:
            p_min = prefixsum[left]
    p_max = prefixsum[right] - p_min
    maximums += p_max

print(prefixsum)