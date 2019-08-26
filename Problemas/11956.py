nCases = int(input())

for x in range(nCases):
	bites = [0] * 100

	line = input()

	index = 0

	for i in line:
		if i == '>':
			index += 1
			if index > 99:
				index = 0
		elif i == '<':
			index -= 1
			if index < 0:
				index = 99
		elif i == '+':
			bites[index] += 1
			if bites[index] > 255:
				bites[index] = 0
		elif i == '-':
			bites[index] -= 1
			if bites[index] < 0:
				bites[index] = 255

	hexBites = []
	for i in bites:
		iStr = ""
		for j in hex(i):
			if type(j) == str:
				iStr += j.upper()
			else:
				iStr += str(j)
			
		hexBites.append(iStr)

	for i in range(len(hexBites)):
		if len(hexBites[i]) >= 4:
			hexBites[i] = hexBites[i][2:]
		else:
			hexBites[i] = hexBites[i][0] + hexBites[i][2]

	hBS = " ".join(hexBites)
	print('Case {}: {}'.format(x + 1, hBS))
