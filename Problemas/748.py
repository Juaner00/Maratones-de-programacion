while True:
	try:
		Rstr, Nstr = map(str, input().split())
		if len(Rstr) == 0:
			break
		Nint = int(Nstr)
		indexL = Rstr.find('.')
		Rstr = Rstr.replace('.', '')

		indexR = (len(Rstr) - indexL) * Nint

		Rint = int(Rstr)
		exp = str(Rint ** Nint)

		expArr = []
		for i in exp:
			expArr.append(i)

		if Rstr[0] == '0':
			ceros = "0" * (indexR - len(expArr))
			expString = "".join(expArr)
			expStr = "." + ceros + expString
		else:
			expArr.insert(len(expArr) - indexR, '.')
			expStr = "".join(expArr)

		expStrip = expStr.strip('0')
		print(expStrip)
	except:
		break
