from encryption import *

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
print("v1.2")
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
	print("╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝v1.2")
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

