from getch import getche

def main():
	# Hace los bloques
	blocks = [[i] for i in range(int(input()))]

	isQuit = False
	while not isQuit:
		msg = ""
		while not isQuit:
			line = getche()
			msg += line
			if msg[-4:] == 'quit':
				isQuit = True
				break

		mA = msg.split()

		print(mA)
		for x in range(0, len(mA) - 4, 4):
			if mA[x] == 'move' and mA[x + 2] == 'onto':
				MoveOnto(mA[x + 1], mA[x + 3], blocks)
			elif mA[x] == 'move' and mA[x + 2] == 'over':
				MoveOver(mA[x + 1], mA[x + 3], blocks)
			elif mA[x] == 'pile' and mA[x + 2] == 'onto':
				PileOnto(mA[x + 1], mA[x + 3], blocks)
			elif mA[x] == 'pile' and mA[x + 2] == 'over':
				PileOver(mA[x + 1], mA[x + 3], blocks)

	# Mostrar blocks
	for i in range(len(blocks)):
		for indJ, j in enumerate(blocks[i]):
			if len(blocks[i]) > 0:
				blocks[i][indJ] = str(j)

	for indI, i in enumerate(blocks):
		num = " ".join(i)
		if len(num) > 0:
			print(str(indI) + ": " + num)
		else:
			print(str(indI) + ":")

def MoveOnto(y, x, blocks):
	index = []
	indexY = []
	# Buscar a y b y quitar los del stack de a y b
	for indI, i in enumerate(blocks):
		if len(i) > 0:
			for indJ, j in enumerate(blocks[indI]):
				if j == int(x):
					index = [indI, indJ]
					for ind, k in enumerate(blocks[indI]):
						if ind > indJ:
							blocks[k].append(k)
							blocks[indI][ind] = None
				if j == int(y):
					indexY = [indI, indJ]
					for ind, k in enumerate(blocks[indI]):
						if ind > indJ:
							blocks[k].append(k)
							blocks[indI][ind] = None

	RemoveNone(blocks)
	# Poner a en b
	blocks[index[0]].append(blocks[indexY[0]][indexY[1]])
	# quitar el que se movió
	blocks[indexY[0]].remove(int(y))

def MoveOver(y, x, blocks):
	index = []
	indexY = []
	# Buscar a y b y quitar los del stack de a
	for indI, i in enumerate(blocks):
		if len(i) > 0:
			for indJ, j in enumerate(blocks[indI]):
				if j == int(y):
					indexY = [indI, indJ]
					for ind, k in enumerate(blocks[indI]):
						if ind > indJ:
							blocks[k].append(k)
							blocks[indI][ind] = None
				if j == int(x):
					index = [indI, indJ]

	RemoveNone(blocks)
	# Poner a en b
	blocks[index[0]].append(blocks[indexY[0]][indexY[1]])
	# quitar el que se movió
	blocks[indexY[0]].remove(int(y))

def PileOnto(y, x, blocks):
	index = []
	indexY = []
	# Buscar a y b y quitar los del stack de a y b
	for indI, i in enumerate(blocks):
		if len(i) > 0:
			for indJ, j in enumerate(blocks[indI]):
				if j == int(x):
					index = [indI, indJ]
					for ind, k in enumerate(blocks[indI]):
						if ind > indJ:
							blocks[k].append(k)
							blocks[indI][ind] = None
				if j == int(y):
					indexY = [indI, indJ]

	# Poner a en b
	for ind in range(indexY[1], len(blocks[indexY[0]])):
		blocks[index[0]].append(blocks[indexY[0]][ind])
		blocks[indexY[0]][ind] = None
	# quitar el que se movió
	RemoveNone(blocks)

def PileOver(y, x, blocks):
	index = []
	indexY = []
	# Buscar a y b y quitar los del stack de a y b
	for indI, i in enumerate(blocks):
		if len(i) > 0:
			for indJ, j in enumerate(blocks[indI]):
				if j == int(x):
					index = [indI, indJ]
				if j == int(y):
					indexY = [indI, indJ]

	# Poner a en b
	for ind in range(indexY[1], len(blocks[indexY[0]])):
		blocks[index[0]].append(blocks[indexY[0]][ind])
		blocks[indexY[0]][ind] = None
	# quitar el que se movió
	RemoveNone(blocks)

def RemoveNone(blocks):
	# Remover None
	for i in range(len(blocks)):
		if len(blocks[i]):
			for j in range(len(blocks[i])):
				try:
					blocks[i].remove(None)
				except:
					None

main()
