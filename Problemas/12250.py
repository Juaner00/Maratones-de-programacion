diccionario = {"HELLO": "ENGLISH", "HOLA": "SPANISH", "HALLO": "GERMAN", "BONJOUR": "FRENCH", "CIAO": "ITALIAN", "ZDRAVSTVUJTE": "RUSSIAN"}

def Main():
	string = input()
	contador = 1
	while (string != "#"):
		try:
			print("Case " + str(contador) + ": " + diccionario[string])
			contador += 1
		except:
			print("UNKNOWN")
		string = input()

Main()
