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
print("v1.1")
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
	print("Output is given down bellow")
	print(PhraseToEncrypt)

elif Type == "e -s":
	FileName = input("Enter Txt name with extention ")
	PhraseToEncrypt = input("Phase to Encrypt ")
	PhraseToEncrypt = PhraseToEncrypt.lower()
	for index in range(NumOfTimes):
		PhraseToEncrypt = Encrypt(PhraseToEncrypt)
	text = open(FileName, "a")
	text.write(PhraseToEncrypt)
	text.close()
	print()
	print("Output is in the scripts folder")

elif Type == "d -r":
	FileName = input("Enter Txt name with extention ")
	PhraseToEncrypt = open(FileName, "r+")
	textfile = PhraseToEncrypt.read()
	textfile = textfile.lower()
	for index in range(NumOfTimes):
		textfile = Decrypt(textfile)
	print()
	print("Output is given down bellow")
	print(textfile)


elif Type == "about":
	print("This is Made By Siddharth Of King siddhu (https://www.youtube.com/channel/UCm-Tcpc9zDONytmwS1Y91-Q)")

elif Type =="help":
	print("\"e\" in the first field encrypts the given text")
	print("\"d\" in the first field Decrypts the encrypted text")
	print("\"e -s\" in the first field Saves the encrypted text in the File name specified")
	print("\"d -r\" in the first field can help you to decrypt txt files sent by the user")
	print("\"about\" for info ")
else:
	print("ERROR WRONG METHOD GIVEN")


Exit = input("Press Enter to exit...")

