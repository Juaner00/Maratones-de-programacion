def Main():
	n1, n2 = map(int, input().split())
	while (n1 != -1 and n2 != -1):
		menor = min(n1, n2)
		mayor = max(n1, n2)
		if (mayor - menor > 100 - mayor + menor):
			print(100 - mayor + menor)
		else:
			print(mayor - menor)
		n1, n2 = map(int, input().split())

Main()
