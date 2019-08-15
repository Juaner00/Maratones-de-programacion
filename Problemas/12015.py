n = int(input())
case = 0
for x in range(0, n):
	case += 1
	sites = {}

	mayor = 0
	for i in range(10):
		site, rank = map(str, input().split())
		sites[site] = int(rank)

		if sites[site] > mayor:
			mayor = sites[site]
	print("Case #{}:".format(case))
	for site in sites:
		if sites[site] == mayor:
			print(site)
