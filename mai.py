n = int(input())
a = list(map(int, input().split()))

maxsum = 0

for i in range(n):
	cursum = sum(a[i:i+3])
	if cursum > maxsum:
		maxsum = cursum
if a[0] + a[-1] + a[-2] > maxsum:
	maxsum = a[0] + a[-1] + a[-2]
if a[0] + a[1] + a[-1] > maxsum:
	maxsum = a[0] + a[1] + a[-1]

print(maxsum)