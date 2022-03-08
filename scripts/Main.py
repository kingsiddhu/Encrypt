#Encrypton


def Encrypt(phrase):
	encrypt = ""
	for letter in phrase:
		if letter in "a":
			encrypt = encrypt + "q"
		elif letter in "b":
			encrypt = encrypt + "w"
		elif letter in "c":
			encrypt = encrypt + "e"
		elif letter in "d":
			encrypt = encrypt + "r"
		elif letter in "e":
			encrypt = encrypt + "t"
		elif letter in "f":
			encrypt = encrypt + "y"
		elif letter in "g":
			encrypt = encrypt + "u"
		elif letter in "h":
			encrypt = encrypt + "i"
		elif letter in "i":
			encrypt = encrypt + "o"
		elif letter in "j":
			encrypt = encrypt + "p"
		elif letter in "k":
			encrypt = encrypt + "1"
		elif letter in "l":
			encrypt = encrypt + "2"
		elif letter in "m":
			encrypt = encrypt + "3"
		elif letter in "n":
			encrypt = encrypt + "4"
		elif letter in "o":
			encrypt = encrypt + "5"
		elif letter in "p":
			encrypt = encrypt + "a"
		elif letter in "q":
			encrypt = encrypt + "s"
		elif letter in "r":
			encrypt = encrypt + "d"
		elif letter in "s":
			encrypt = encrypt + "f"
		elif letter in "t":
			encrypt = encrypt + "g"
		elif letter in "u":
			encrypt = encrypt + "h"
		elif letter in "v":
			encrypt = encrypt + "j"
		elif letter in "w":
			encrypt = encrypt + "k"
		elif letter in "x":
			encrypt = encrypt + "l"
		elif letter in "y":
			encrypt = encrypt + "6"
		elif letter in "z":
			encrypt = encrypt + "7"
		elif letter in "1":
			encrypt = encrypt + "8"
		elif letter in "2":
			encrypt = encrypt + "9"
		elif letter in "3":
			encrypt = encrypt + "0"
		elif letter in "4":
			encrypt = encrypt + "z"
		elif letter in "5":
			encrypt = encrypt + "x"
		elif letter in "6":
			encrypt = encrypt + "c"
		elif letter in "7":
			encrypt = encrypt + "v"
		elif letter in "8":
			encrypt = encrypt + "b"
		elif letter in "9":
			encrypt = encrypt + "n"
		elif letter in "0":
			encrypt = encrypt + "m"
		else:
			encrypt = encrypt + letter
	return encrypt



#DeCryption


def Decrypt(phrase):
	decrypt = ""
	for en in phrase:
		if en in "q":
			decrypt = decrypt + "a"
		elif en in "w":
			decrypt = decrypt + "b"
		elif en in "e":
			decrypt = decrypt + "c"
		elif en in "r":
			decrypt = decrypt + "d"
		elif en in "t":
			decrypt = decrypt + "e"
		elif en in "y":
			decrypt = decrypt + "f"
		elif en in "u":
			decrypt = decrypt + "g"
		elif en in "i":
			decrypt = decrypt + "h"
		elif en in "o":
			decrypt = decrypt + "i"
		elif en in "p":
			decrypt = decrypt + "j"
		elif en in "1":
			decrypt = decrypt + "k"
		elif en in "2":
			decrypt = decrypt + "l"
		elif en in "3":
			decrypt = decrypt + "m"
		elif en in "4":
			decrypt = decrypt + "n"
		elif en in "5":
			decrypt = decrypt + "o"
		elif en in "a":
			decrypt = decrypt + "p"
		elif en in "s":
			decrypt = decrypt + "q"
		elif en in "d":
			decrypt = decrypt + "r"
		elif en in "f":
			decrypt = decrypt + "s"
		elif en in "g":
			decrypt = decrypt + "t"
		elif en in "h":
			decrypt = decrypt + "u"
		elif en in "j":
			decrypt = decrypt + "v"
		elif en in "k":
			decrypt = decrypt + "w"
		elif en in "l":
			decrypt = decrypt + "x"
		elif en in "6":
			decrypt = decrypt + "y"
		elif en in "7":
			decrypt = decrypt + "z"
		elif en in "8":
			decrypt = decrypt + "1"
		elif en in "9":
			decrypt = decrypt + "2"
		elif en in "0":
			decrypt = decrypt + "3"
		elif en in "z":
			decrypt = decrypt + "4"
		elif en in "x":
			decrypt = decrypt + "5"
		elif en in "c":
			decrypt = decrypt + "6"
		elif en in "v":
			decrypt = decrypt + "7"
		elif en in "b":
			decrypt = decrypt + "8"
		elif en in "n":
			decrypt = decrypt + "9"
		elif en in "m":
			decrypt = decrypt + "0"
		
		else:
			decrypt = decrypt + en
	return decrypt

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

print("Use This Program To Encrypt or Decrypt Text \nThanks for useing this Program All writen by Siddharth\nThe Encryption Number Must be Informed to the Reciver to Decrypt\nFor help Type Help in the first field\nUSE THE SAME PROGRAM VERSION TO PREVENT PROBLEMS")
print("v1.3")
print("")
#Inputs

Type = input("Type e to encrypt, d to decrypt and info for info ")
NumOfTimes = int(input("Enter The Encryption Number "))


#Mains
if Type == "e":
	PhraseToEncrypt = input("Phase to Encrypt ")
	PhraseToEncrypt = PhraseToEncrypt.lower()
	for index in range(NumOfTimes):
		PhraseToEncrypt = Encrypt(PhraseToEncrypt)
	print()
	print("Output is given down bellow")
	print(PhraseToEncrypt)

elif Type == "d":
	PhraseToEncrypt = input("Phase to Encrypt ")
	PhraseToEncrypt = PhraseToEncrypt.lower()
	for index in range(NumOfTimes):
		PhraseToEncrypt = Decrypt(PhraseToEncrypt)
	print()
	print("Output is given down below")
	print(PhraseToEncrypt)

elif Type == "e -s":
	FileName = input("Enter Txt name ")
	PhraseToEncrypt = input("Phase to Encrypt ")
	PhraseToEncrypt = PhraseToEncrypt.lower()
	for index in range(NumOfTimes):
		PhraseToEncrypt = Encrypt(PhraseToEncrypt)
	text = (FileName + ".enc")
	text = open(text, "a")
	text.write(PhraseToEncrypt)
	text.close()
	print()
	print("Output is in the folder of the program" , FileName + ".enc")

elif Type == "d -r":
	FileName = input("Enter Txt name ")
	PhraseToEncrypt = open(FileName + ".enc", "r+")
	textfile = PhraseToEncrypt.read()
	textfile = textfile.lower()
	for index in range(NumOfTimes):
		textfile = Decrypt(textfile)
	print()
	print("Output is given down below")
	print(textfile)

elif Type == "e -r -s":
	FileName = input("Enter Encrypted file name ")    #enc
	SaveFile = input("File to Encrypt ")    #txt
	File = (SaveFile + ".txt")              #txt
	File = open(File, "r+")                #txt
	encrypt = File.read()                   #txt
	encrypt = encrypt.lower()               #txt
	for index in range(NumOfTimes):
		encrypt = Encrypt(encrypt)
	SaveFile = (SaveFile + ".enc")
	text = open(SaveFile, "a")
	text.write(encrypt)
	text.close()
	print()
	print("Output is in the folder of the program" , SaveFile + ".enc")

elif Type == "d -r -s":
	FileName = input("Enter Txt name ")    #.txt
	SaveFile = input("File to Decrypt ")  #.enc
	Fileenc = (SaveFile + ".enc")         #.enc
	Fileenc = open(Fileenc, "r+")            #.enc
	encrypt = Fileenc.read()              #.enc
	encrypt = encrypt.lower()          #.enc
	for index in range(NumOfTimes):
		encrypt = Decrypt(encrypt)
	text = open(FileName + ".txt", "a")   
	text.write(encrypt)
	text.close()
	print()
	print("Output is in the folder of the program" , FileName + ".txt")
	


elif Type == "about":
	print("███████╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗██╗░█████╗░███╗░░██╗")
	print("██╔════╝████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║")
	print("█████╗░░██╔██╗██║██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║██║░░██║██╔██╗██║")
	print("██╔══╝░░██║╚████║██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║██║░░██║██║╚████║")
	print("███████╗██║░╚███║╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░██║╚█████╔╝██║░╚███║")
	print("╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝v1.3")
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
	print("\"about\" for info ")
else:
	print("ERROR WRONG METHOD GIVEN")


Exit = input("Press Enter to exit...")

