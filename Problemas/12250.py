diccionario = {"HELLO": "ENGLISH", "HOLA": "SPANISH", "HALLO": "GERMAN", "BONJOUR": "FRENCH", "CIAO": "ITALIAN", "ZDRAVSTVUJTE": "RUSSIAN"}

def Main():
	string = input()
	contador = 0
	while (string != "#"):
		contador += 1
		try:
			print("Case " + str(contador) + ": " + diccionario[string])
		except:
			print("Case " + str(contador) + ": " + "UNKNOWN")
		string = input()

Main()
