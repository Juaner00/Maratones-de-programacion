case = 1
while True:
	inp = int(input())

	if inp < 0:
		break

	pastes = 0
	acum = 1

	while acum < inp:
		acum *= 2
		pastes += 1

	print(f'Case {case}: {pastes}')
	case += 1