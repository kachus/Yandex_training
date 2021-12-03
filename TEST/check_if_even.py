num = int(input())
def is_even(num):
	return num == (num>>1)<<1
print(is_even(num))
