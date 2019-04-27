
N, Q = map(int, input().split())

lastAnswer = 0
seqList = [ [] for _ in range(N) ]

for i in range(Q):
	q, x, y = map(int, input().split())
	index = (x ^ lastAnswer) % N
	seq = seqList[index]
	if q == 1:
		seq.append(y)
	elif q == 2:
		lastAnswer = seq[y % len(seq)]
		print(lastAnswer)
	else:
		raise ValueError()
