""" LARGE
for i in range(int(input())):
	line = input()
	contM = line.count('M')
	contF = line.count('F')
	if contM == contF and len(line) != 2:
	  	print("LOOP")
	else:
		print("NO LOOP")	
"""

""" MEDIUM
for i in range(int(input())):
	line = input()
	contM = line.count('M')
	contF = line.count('F')
	print("LOOP") if contM == contF and len(line) != 2 else print("NO LOOP")	
"""	

""" SHORT """
for i in range(int(input())):
	line = input()
	print("LOOP") if line.count('M') == line.count('F') and len(line) != 2 else print("NO LOOP")		
