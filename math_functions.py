"""
	Implementing math functions related to statistics in raw Python code
"""

def arithmetic_mean(arr):
	return sum(arr) / len(arr)

def median(arr):
	n = len(arr)
	ar = sorted(arr)
	if n&1 == 0:
		n1 = int((n-1)/2)
		n2 = int((n+1)/2)
		return (ar[n1] + ar[n2])/2
	return ar[int(n/2)]

def mode(arr):
	di = {}
	for i in arr:
		if di.get(i,0) == 0:
			di[i] = 1
		else:
			di[i] += 1
	mx,vl = -10**9,None
	for i in di.keys():
		if di[i] > mx:
			mx = di[i]
			vl = i
	return vl

def standard_dev(arr):
	mu = arithmetic_mean(arr)
	variance = 0
	for i in arr:
		variance += (mu - i)*(mu - i)
	variance /= len(arr)
	return variance**0.5

print(median([1,2,3,4,5]))
print(mode([2,2,3,3,3,3,4,4,4,4,4]))
print(standard_dev([i for i in range(1,101)]))


