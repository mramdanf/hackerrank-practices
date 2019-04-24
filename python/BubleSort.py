
# Tracing

# n: 3
# if a[j] > a[j+1]
# 	// Swap
# 	a[j] = a[j+1]
# 	a[j+1] = a[j]

# [3,2,1] intial

# i: 0
# j: 0
# [2,3,1]
# n-i-1: 2


# i: 0
# j: 0 1
# [2,1,3]
# n-i-1: 2

# ---------------------

# i: 0 1
# j: 0
# [1,2,3]
# n-i-1: 1

def countSwaps(a):
	n = len(a)
	swap = 0

	for i in range(n):
		for j in range(0, n-i-1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
				swap += 1

	print('Array is sorted in %d swaps.' % (swap))
	print('First Element: %d' % (a[0]))
	print('Last Element: %d' % (a[len(a) - 1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

