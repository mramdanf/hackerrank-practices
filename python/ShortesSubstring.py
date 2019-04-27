
s = 'dabbcabcd'
n = len(s)
setOfChar = set(s)
lenSubs = []

dictOfChars = []
for c in setOfChar:
	item = {
		'char': c,
		'count': 0
	}
	dictOfChars.append(item)

start = 0
allFound = True

while start < n and allFound == True:
	for i in range(start, n):
		for d in range(0, len(dictOfChars)):
			if dictOfChars[d]['char'] == s[i]: 
				dictOfChars[d]['count'] += 1

		
	allFound = False
		# Cek apakah masih ada yg countnya 0
		# for doc in dictOfChars:
		# 	if doc['count'] == 0:
		# 		allFound = False
		
		# if allFound:
		# 	lenSubs.append(s[start-i])
		# 	start = i
		# 	break
print(dictOfChars)

