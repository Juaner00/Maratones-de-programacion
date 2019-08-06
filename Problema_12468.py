def Main():
	s1, s2, s3 = int(input()), int(input()), int(input())
	while (s1 != 0 and s2 != 0 and s3 != 0):
		if (s1**2 + s2**2 == s3**2):
			print("right")
		else:
			print("wrong")
		s1, s2, s3 = int(input()), int(input()), int(input())

Main()
