import os
import time
def Encrypt(phrase):
	encrypt = ""
	for en in phrase:
		if en in "a":
			encrypt = encrypt + "`"
		elif en in "b":
			encrypt = encrypt + "1"
		elif en in "c":
			encrypt = encrypt + "q"
		elif en in "d":
			encrypt = encrypt + "a"
		elif en in "e":
			encrypt = encrypt + "z"
		elif en in "f":
			encrypt = encrypt + "2"
		elif en in "g":
			encrypt = encrypt + "w"
		elif en in "h":
			encrypt = encrypt + "s"
		elif en in "i":
			encrypt = encrypt + "x"
		elif en in "j":
			encrypt = encrypt + "3"
		elif en in "k":
			encrypt = encrypt + "e"
		elif en in "l":
			encrypt = encrypt + "d"
		elif en in "m":
			encrypt = encrypt + "c"
		elif en in "n":
			encrypt = encrypt + "4"
		elif en in "o":
			encrypt = encrypt + "r"
		elif en in "p":
			encrypt = encrypt + "f"
		elif en in "q":
			encrypt = encrypt + "v"
		elif en in "r":
			encrypt = encrypt + "5"
		elif en in "s":
			encrypt = encrypt + "t"
		elif en in "t":
			encrypt = encrypt + "g"
		elif en in "u":
			encrypt = encrypt + "b"
		elif en in "v":
			encrypt = encrypt + "6"
		elif en in "w":
			encrypt = encrypt + "y"
		elif en in "x":
			encrypt = encrypt + "h"
		elif en in "y":
			encrypt = encrypt + "n"
		elif en in "z":
			encrypt = encrypt + "7"
		elif en in "1":
			encrypt = encrypt + "u"
		elif en in "2":
			encrypt = encrypt + "j"
		elif en in "3":
			encrypt = encrypt + "m"
		elif en in "4":
			encrypt = encrypt + "8"
		elif en in "5":
			encrypt = encrypt + "i"
		elif en in "6":
			encrypt = encrypt + "k"
		elif en in "7":
			encrypt = encrypt + ","
		elif en in "8":
			encrypt = encrypt + "9"
		elif en in "9":
			encrypt = encrypt + "o"
		elif en in "0":
			encrypt = encrypt + "l"
		elif en in "-":
			encrypt = encrypt + "."
		elif en in "=":
			encrypt = encrypt + "0"
		elif en in "[":
			encrypt = encrypt + "p"
		elif en in "]":
			encrypt = encrypt + ";"
		elif en in "£":
			encrypt = encrypt + "/"
		elif en in ";":
			encrypt = encrypt + "-"
		elif en in "'":
			encrypt = encrypt + "["
		elif en in ",":
			encrypt = encrypt + "'"
		elif en in ".":
			encrypt = encrypt + "="
		elif en in "/":
			encrypt = encrypt + "]"
		elif en in "`":
			encrypt = encrypt + "£"
		elif en in "~":
			encrypt = encrypt + "|"
		elif en in "!":
			encrypt = encrypt + "}"
		elif en in "@":
			encrypt = encrypt + "+"
		elif en in "#":
			encrypt = encrypt + '"'
		elif en in "$":
			encrypt = encrypt + "{"
		elif en in "%":
			encrypt = encrypt + "_"
		elif en in "^":
			encrypt = encrypt + "?"
		elif en in "&":
			encrypt = encrypt + ":"
		elif en in "*":
			encrypt = encrypt + "P"
		elif en in "(":
			encrypt = encrypt + ")"
		elif en in ")":
			encrypt = encrypt + ">"
		elif en in "_":
			encrypt = encrypt + "L"
		elif en in "+":
			encrypt = encrypt + "O"
		elif en in "{":
			encrypt = encrypt + "("
		elif en in "}":
			encrypt = encrypt + "<"
		elif en in "|":
			encrypt = encrypt + "K"
		elif en in ":":
			encrypt = encrypt + "I"
		elif en in '"':
			encrypt = encrypt + "*"
		elif en in "<":
			encrypt = encrypt + "M"
		elif en in ">":
			encrypt = encrypt + "J"
		elif en in "?":
			encrypt = encrypt + "U"
		elif en in "Q":
			encrypt = encrypt + "&"
		elif en in "W":
			encrypt = encrypt + "N"
		elif en in "E":
			encrypt = encrypt + "H"
		elif en in "R":
			encrypt = encrypt + "Y"
		elif en in "T":
			encrypt = encrypt + "^"
		elif en in "Y":
			encrypt = encrypt + "B"
		elif en in "U":
			encrypt = encrypt + "G"
		elif en in "I":
			encrypt = encrypt + "T"
		elif en in "O":
			encrypt = encrypt + "%"
		elif en in "P":
			encrypt = encrypt + "V"
		elif en in "A":
			encrypt = encrypt + "F"
		elif en in "S":
			encrypt = encrypt + "R"
		elif en in "D":
			encrypt = encrypt + "$"
		elif en in "F":
			encrypt = encrypt + "C"
		elif en in "G":
			encrypt = encrypt + "D"
		elif en in "H":
			encrypt = encrypt + "E"
		elif en in "J":
			encrypt = encrypt + "#"
		elif en in "K":
			encrypt = encrypt + "X"
		elif en in "L":
			encrypt = encrypt + "S"
		elif en in "Z":
			encrypt = encrypt + "W"
		elif en in "X":
			encrypt = encrypt + "@"
		elif en in "C":
			encrypt = encrypt + "Z"
		elif en in "V":
			encrypt = encrypt + "A"
		elif en in "B":
			encrypt = encrypt + "Q"
		elif en in "N":
			encrypt = encrypt + " "
		elif en in "M":
			encrypt = encrypt + "!"
		elif en in " ":
			encrypt = encrypt + "~"
		else:
			encrypt = encrypt + en
	return encrypt

def Decrypt(phrase):
	encrypt = ""
	for en in phrase:
		if en in "`":
			encrypt = encrypt + "a"
		elif en in "1":
			encrypt = encrypt + "b"
		elif en in "q":
			encrypt = encrypt + "c"
		elif en in "a":
			encrypt = encrypt + "d"
		elif en in "z":
			encrypt = encrypt + "e"
		elif en in "2":
			encrypt = encrypt + "f"
		elif en in "w":
			encrypt = encrypt + "g"
		elif en in "s":
			encrypt = encrypt + "h"
		elif en in "x":
			encrypt = encrypt + "i"
		elif en in "3":
			encrypt = encrypt + "j"
		elif en in "e":
			encrypt = encrypt + "k"
		elif en in "d":
			encrypt = encrypt + "l"
		elif en in "c":
			encrypt = encrypt + "m"
		elif en in "4":
			encrypt = encrypt + "n"
		elif en in "r":
			encrypt = encrypt + "o"
		elif en in "f":
			encrypt = encrypt + "p"
		elif en in "v":
			encrypt = encrypt + "q"
		elif en in "5":
			encrypt = encrypt + "r"
		elif en in "t":
			encrypt = encrypt + "s"
		elif en in "g":
			encrypt = encrypt + "t"
		elif en in "b":
			encrypt = encrypt + "u"
		elif en in "6":
			encrypt = encrypt + "v"
		elif en in "y":
			encrypt = encrypt + "w"
		elif en in "h":
			encrypt = encrypt + "x"
		elif en in "n":
			encrypt = encrypt + "y"
		elif en in "7":
			encrypt = encrypt + "z"
		elif en in "u":
			encrypt = encrypt + "1"
		elif en in "j":
			encrypt = encrypt + "2"
		elif en in "m":
			encrypt = encrypt + "3"
		elif en in "8":
			encrypt = encrypt + "4"
		elif en in "i":
			encrypt = encrypt + "5"
		elif en in "k":
			encrypt = encrypt + "6"
		elif en in ",":
			encrypt = encrypt + "7"
		elif en in "9":
			encrypt = encrypt + "8"
		elif en in "o":
			encrypt = encrypt + "9"
		elif en in "l":
			encrypt = encrypt + "0"
		elif en in ".":
			encrypt = encrypt + "-"
		elif en in "0":
			encrypt = encrypt + "="
		elif en in "p":
			encrypt = encrypt + "]"
		elif en in ";":
			encrypt = encrypt + "]"
		elif en in "/":
			encrypt = encrypt + "£"
		elif en in "-":
			encrypt = encrypt + ";"
		elif en in "[":
			encrypt = encrypt + "'"
		elif en in "'":
			encrypt = encrypt + ","
		elif en in "=":
			encrypt = encrypt + "."
		elif en in "]":
			encrypt = encrypt + "/"
		elif en in "£":
			encrypt = encrypt + "`"
		elif en in "|":
			encrypt = encrypt + "~"
		elif en in "}":
			encrypt = encrypt + "!"
		elif en in "+":
			encrypt = encrypt + "@"
		elif en in '"':
			encrypt = encrypt + '#'
		elif en in "{":
			encrypt = encrypt + "$"
		elif en in "_":
			encrypt = encrypt + "%"
		elif en in "?":
			encrypt = encrypt + "^"
		elif en in ":":
			encrypt = encrypt + "&"
		elif en in "P":
			encrypt = encrypt + "*"
		elif en in ")":
			encrypt = encrypt + "("
		elif en in ">":
			encrypt = encrypt + ")"
		elif en in "L":
			encrypt = encrypt + "_"
		elif en in "O":
			encrypt = encrypt + "+"
		elif en in "(":
			encrypt = encrypt + "{"
		elif en in "<":
			encrypt = encrypt + "}"
		elif en in "K":
			encrypt = encrypt + "|"
		elif en in "I":
			encrypt = encrypt + ":"
		elif en in '*':
			encrypt = encrypt + '"'
		elif en in "M":
			encrypt = encrypt + "<"
		elif en in "J":
			encrypt = encrypt + ">"
		elif en in "U":
			encrypt = encrypt + "?"
		elif en in "&":
			encrypt = encrypt + "Q"
		elif en in "N":
			encrypt = encrypt + "W"
		elif en in "H":
			encrypt = encrypt + "E"
		elif en in "Y":
			encrypt = encrypt + "R"
		elif en in "^":
			encrypt = encrypt + "T"
		elif en in "B":
			encrypt = encrypt + "Y"
		elif en in "G":
			encrypt = encrypt + "U"
		elif en in "T":
			encrypt = encrypt + "I"
		elif en in "%":
			encrypt = encrypt + "O"
		elif en in "V":
			encrypt = encrypt + "P"
		elif en in "F":
			encrypt = encrypt + "A"
		elif en in "R":
			encrypt = encrypt + "S"
		elif en in "$":
			encrypt = encrypt + "D"
		elif en in "C":
			encrypt = encrypt + "F"
		elif en in "D":
			encrypt = encrypt + "G"
		elif en in "E":
			encrypt = encrypt + "H"
		elif en in "#":
			encrypt = encrypt + "J"
		elif en in "X":
			encrypt = encrypt + "K"
		elif en in "S":
			encrypt = encrypt + "L"
		elif en in "W":
			encrypt = encrypt + "Z"
		elif en in "@":
			encrypt = encrypt + "X"
		elif en in "Z":
			encrypt = encrypt + "C"
		elif en in "A":
			encrypt = encrypt + "V"
		elif en in "Q":
			encrypt = encrypt + "B"
		elif en in " ":
			encrypt = encrypt + "N"
		elif en in "!":
			encrypt = encrypt + "M"
		elif en in "~":
			encrypt = encrypt + " "
		else:
			encrypt = encrypt + en
	return encrypt
import json
#Title
print("                                                                                    ")
print("     ███████╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗██╗░█████╗░███╗░░██╗")
print("     ██╔════╝████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║")
print("     █████╗░░██╔██╗██║██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║██║░░██║██╔██╗██║")
print("     ██╔══╝░░██║╚████║██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║██║░░██║██║╚████║")
print("     ███████╗██║░╚███║╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░██║╚█████╔╝██║░╚███║")
print("     ╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝")
print("                                                                                    ")
#texts

print("Use This Program To Encrypt or Decrypt Text. Thanks for using this Program.\nAll of it is writen by Siddharth, The Encryption Number Must be Informed to the Reciver to Decrypt\nFor help Type about in the first field\n\nUSE THE SAME PROGRAM VERSION TO PREVENT PROBLEMS")
print("presets can be used instead of key")
print("v1.7")
print("encryption v1.3")
print("")
#Inputs

try:
	# Opening JSON file
    with open('settings.json', 'r') as openfile:
        settings = json.load(openfile)

except:
	print("settings file not found")
	settings ={
    "Defaultcount" : 128,
    "ShowOriginal" : False,
    "CustomPreset" : 1000,
    "CustomPreset2" : 1001
}
	with open("settings.json", "w") as outfile:
		json.dump(settings, outfile)

Type = input("Type e to encrypt, d to decrypt and info for info: ")
NumOfTimes = input("Enter The key: ")

try:
	if NumOfTimes in settings:
		print("\nPreset chosen " + NumOfTimes + "\n")
		NumOfTimes = settings[NumOfTimes]
		NumOfTimes = int(NumOfTimes)
	elif NumOfTimes == "":
		NumOftimes = int(settings["Defaultcount"])
	else:
		NumOfTimes = int(NumOfTimes)
except ValueError:
	print("Error...")



#Mains
if Type == "e":
	PhraseToEncrypt = input("Phase to Encrypt ")
	origianl = PhraseToEncrypt
	if NumOfTimes < 5000:
		print("\nDecrypting your message...\n")
		time.sleep(2)
		print("Stand by, almost finished...\n")
		time.sleep(2)
	else:
		print("\nDecrypting your message...\n")
		print("Since the key is higher than 5000, I am taking time...")
	#PhraseToEncrypt = PhraseToEncrypt.lower()
	for index in range(NumOfTimes):
		PhraseToEncrypt = Encrypt(PhraseToEncrypt)
	print()
	if settings["ShowOriginal"] == True:
		print("\nOriginal Phrase: " + origianl + "\n")

	print("Output is given down bellow")
	print(PhraseToEncrypt)

elif Type == "d":
	PhraseToEncrypt = input("Phase to Encrypt ")
	origianl = PhraseToEncrypt
	if int(NumOfTimes) < 5000:
		print("\nDecrypting your message...\n")
		time.sleep(2)
		print("Stand by, almost finished...\n")
		time.sleep(2)
	else:
		print("\nDecrypting your message...\n")
		print("Since the key is higher than 5000, I am taking time...")
	#PhraseToEncrypt = PhraseToEncrypt.lower()
	for index in range(NumOfTimes):
		PhraseToEncrypt = Decrypt(PhraseToEncrypt)
	print()
	if settings["ShowOriginal"] == True:
		print("\nOriginal Phrase: " + origianl + "\n")
	print("Output is given down below")
	print(PhraseToEncrypt)

elif Type == "e -s":
	FileName = input("Enter Txt name ")
	PhraseToEncrypt = input("Phase to Encrypt ")
	#PhraseToEncrypt = PhraseToEncrypt.lower()
	origianl = PhraseToEncrypt
	if int(NumOfTimes) < 5000:
		print("\nDecrypting your message...\n")
		time.sleep(2)
		print("Stand by, almost finished...\n")
		time.sleep(2)
	else:
		print("\nDecrypting your message...\n")
		print("Since the key is higher than 5000, I am taking time...")
	for index in range(NumOfTimes):
		PhraseToEncrypt = Encrypt(PhraseToEncrypt)
	text = (FileName + ".enc")
	text = open(text, "a")
	text.write(PhraseToEncrypt)
	text.close()
	print()
	if settings["ShowOriginal"] == True:
		print("\nOriginal Phrase: " + origianl + "\n")
	print("Output is in the folder of the program" , FileName + ".enc")

elif Type == "d -r":
	print("\n")
	for a in os.listdir():
		print(a)
	print("\n")
	FileName = input("Enter Txt name ")
	PhraseToEncrypt = open(FileName + ".enc", "r+")
	textfile = PhraseToEncrypt.read()
	origianl = textfile
	if int(NumOfTimes) < 5000:
		print("\nDecrypting your message...\n")
		time.sleep(2)
		print("Stand by, almost finished...\n")
		time.sleep(2)
	else:
		print("\nDecrypting your message...\n")
		print("Since the key is higher than 5000, I am taking time...")
	#textfile = textfile.lower()
	for index in range(NumOfTimes):
		textfile = Decrypt(textfile)
	print()
	if settings["ShowOriginal"] == True:
		print("\nOriginal Phrase: " + origianl + "\n")
	print("Output is given down below")
	print(textfile)

elif Type == "e -r -s":
	print("\n")
	for a in os.listdir():
		print(a)
	print("\n")
	FileName = input("Enter Encrypted file name ")    #enc
	SaveFile = input("File to Encrypt ")    #txt
	File = (SaveFile + ".txt")              #txt
	File = open(File, "r+")                #txt
	encrypt = File.read()                   #txt
	#encrypt = encrypt.lower()               #txt
	if int(NumOfTimes) < 5000:
		print("\nDecrypting your message...\n")
		time.sleep(2)
		print("Stand by, almost finished...\n")
		time.sleep(2)
	else:
		print("\nDecrypting your message...\n")
		print("Since the key is higher than 5000, I am taking time...")
	for index in range(NumOfTimes):
		encrypt = Encrypt(encrypt)
	SaveFile = (SaveFile + ".enc")
	text = open(SaveFile, "a")
	text.write(encrypt)
	text.close()
	print()
	print("Output is in the folder of the program" , SaveFile)

elif Type == "d -r -s":
	print("\n")
	for a in os.listdir():
		print(a)
	print("\n")
	FileName = input("Enter Txt name ")    #.txt
	SaveFile = input("File to Decrypt ")  #.enc
	Fileenc = (SaveFile + ".enc")         #.enc
	Fileenc = open(Fileenc, "r+")            #.enc
	encrypt = Fileenc.read()              #.enc
	#encrypt = encrypt.lower()          #.enc
	if int(NumOfTimes) < 5000:
		print("\nDecrypting your message...\n")
		time.sleep(2)
		print("Stand by, almost finished...\n")
		time.sleep(2)
	else:
		print("\nDecrypting your message...\n")
		print("Since the key is higher than 5000, I am taking time...")
	for index in range(NumOfTimes):
		encrypt = Decrypt(encrypt)
	text = open(FileName + ".txt", "a")   
	text.write(encrypt)
	text.close()
	print()
	print("Output is in the folder of the program" , FileName)

elif Type == "add":
	preset = input("Input Preset Name: ")
	key = input("input Preset value: ")
	print("Adding your preset...")
	time.sleep(2)
	with open("settings.json") as json_file:
		json_decoded = json.load(json_file)

	json_decoded[preset] = key

	with open("settings.json", 'w') as json_file:
		json.dump(json_decoded, json_file)
	print("Preset Added!")

elif Type == "about":
	print("\n")
	print("███████╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗██╗░█████╗░███╗░░██╗")
	print("██╔════╝████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║")
	print("█████╗░░██╔██╗██║██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║██║░░██║██╔██╗██║")
	print("██╔══╝░░██║╚████║██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║██║░░██║██║╚████║")
	print("███████╗██║░╚███║╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░██║╚█████╔╝██║░╚███║")
	print("╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝v1.7")
	print("")
	print("Hi I am Siddharth")
	print("")
	print("## Instructions to start")
	print("")
	print("For windows users Run the batch file (.bat)")
	print("For Mac and Linix users Open the `scripts\Main.py` With Python Installed [Python Website](https://www.python.org/)")
	print("")
	print("## App Instructions")
	print(" - Type \"e\" in the field given to encrypt")
	print(" - Type the number of time for the Program to encrypt the sentence")
	print(" - Type the Phrase to be encrypted")
	print(" - You Recive a Scrambled Word")
	print("")
	print(" - The Number and scrambled Phrase must be given to the Reciver")
	print(" - The Reciver Must Type \"d\" to Decrypt the word Given")
	print(" - The Reciver Must Type in the number used for encrypting the word (Number of time the program must encrypt used before)")
	print(" - Then the sentence given")
	print(" - The program will Show the sentence")
	print("")
	print("Note that the program for now only encrypts a-z and 0-9 other symbols wont be encrypted and will show as it is")
	print("")
	print("This software is and always will be free, but if you support the development, it will be largely appreciated:")
	print("")
	print("Ethererm Address : 0x448A558863DBA1e3392Cd0a80ea497c06821d2aA (I use MetaMask hence the repeted address)")
	print(" Binance Address : 0x448A558863DBA1e3392Cd0a80ea497c06821d2aA")
	print(" Polygon Address : 0x448A558863DBA1e3392Cd0a80ea497c06821d2aA")
	print(" Bitcoin Address : 177fzZh3t3cPccAeX4bTpVW5tAEkzZSB7V")
	print("    Doge Address : DNTouZp7GsbqNbA7xjrqJwDvfD1Y9qHPDv")
	print("This is Made By Siddharth Of King siddhu (https://www.youtube.com/channel/UCm-Tcpc9zDONytmwS1Y91-Q)")

elif Type =="help":
	print("\"e\" in the first field encrypts the given text")
	print("\"d\" in the first field Decrypts the encrypted text")
	print("\"e -s\" in the first field Saves the encrypted text in the File name specified")
	print("\"d -r\" in the first field can help you to decrypt  files sent by the user")
	print("\"e -r -s\" in the first field Encrypts the text file given and save it in enc format")
	print("\"d -r -s\" in the first field can help you to decrypt txt files sent by the user and save it")
	print('"add" to add a preset for ease.')
	print('"TriggerOriginal"')
	print("\"about\" for info ")
elif Type == "TriggerOriginal":
	if settings["ShowOriginal"] == True:
		print("Changing settings...")
		time.sleep(1)
		
		with open("settings.json") as json_file:
			settings = json.load(json_file)

			settings["ShowOriginal"] = False

		with open("settings.json", 'w') as json_file:
			json.dump(settings, json_file)
	elif settings["ShowOriginal"] == False:
		print("Changing settings...")
		time.sleep(1)
		
		with open("settings.json") as json_file:
			settings = json.load(json_file)

			settings["ShowOriginal"] = True

		with open("settings.json", 'w') as json_file:
			json.dump(settings, json_file)
	else:
		with open("settings.json") as json_file:
			json_decoded = json.load(json_file)

			json_decoded["ShowOriginal"] = False

		with open("settings.json", 'w') as json_file:
			json.dump(json_decoded, json_file)
else:
	print("ERROR WRONG METHOD GIVEN")


Exit = input("Press Enter to exit...")

