def Main():
	s1, s2, s3 = map(int, input().split())
	while (s1 != 0 and s2 != 0 and s3 != 0):
		esc1 = s1*s1
		esc2 = s2*s2
		esc3 = s3*s3
		if ((esc1 + esc2 == esc3) or (esc3 + esc2 == esc1) or (esc1 + esc3 == esc2)):
			print("right")
		else:
			print("wrong")
		s1, s2, s3 = map(int, input().split())

Main()
