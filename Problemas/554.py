def main():
	alf = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	dic = []
	line = input()
	while line != '#':
		dic.append(line)
		line = input()

	enc = []
	for char in input():
		enc.append(char)

	indexOr = []
	for ind, char in enumerate(enc):
		indexOr.append(alf.find(char))

	mayor = 0
	shiftMayor = 0

	for shift in range(1, len(alf)):
		encCopy = enc
		msg = ''.join(encCopy)

		match = 0
		for word in msg.split():
			if word in dic:
				match += 1
			if match > mayor:
				mayor = match 
				shiftMayor = shift - 1

		for index, char in enumerate(encCopy):
			encCopy[index] = alf[indexOr[index] - shift]
		
	for index, char in enumerate(enc):
		enc[index] = alf[indexOr[index] - shiftMayor]
	
	print(''.join(enc), end="")
	
if __name__ == '__main__':
    main()
