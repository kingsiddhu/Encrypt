def Encrypt(phrase, NumOfTimes=1):
    """
    This Encrypts your phrase
    """
    before = r"""qwertyuiopasdfghjklzxcvbnm1234567890`-=]£;',./ QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()~_+{}|:"<>?"""
    afters = r"""aM6 ABCDE=N[]£127890-defghijklm3VWXYxyz,"{nop4.~!@#$%^Z<>?:5}|_+tbcFGHIJKLuvw&*()OPQRSTUqrs/;'"""
    encrypt = ''
    for en in phrase:
        if en == "\n":
            encrypt = encrypt + "\n"
        elif before.find(en) == -1:
            encrypt = encrypt + en
        else:
            encrypt = encrypt + afters[before.find(en)]
    return encrypt


#DeCryption


def Decrypt(phrase):
    """
    This Decrypts your phrase
    """
    before = r"""qwertyuiopasdfghjklzxcvbnm1234567890`-=]£;',./ QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()~_+{}|:"<>?"""
    afters = r"""aM6 ABCDE=N[]£127890-defghijklm3VWXYxyz,"{nop4.~!@#$%^Z<>?:5}|_+tbcFGHIJKLuvw&*()OPQRSTUqrs/;'"""
    encrypt = ""
    for en in phrase:
        if en == "\n":
            encrypt = encrypt + "\n"
        elif before.find(en) == -1:
            encrypt = encrypt + en
        else:
            encrypt = encrypt + before[afters.find(en)]
    return encrypt

import os
import time
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
print("v1.8")
print("encryption v2")
print("")
#Inputs

try:
	# Opening JSON file
    with open('settings.json', 'r') as openfile:
        settings = json.load(openfile)

except:
	print("Settings file not found\n\r")
	settings ={
    "Defaultcount" : 128,
    "ShowOriginal" : False,
    "CustomPreset" : 1000,
    "CustomPreset2" : 1001,
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
	FileName = input("Enter file name to save as: ")
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
	FileName = input("Enter The .enc file name: ")
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
	SaveFile = input("File name to Encrypt ")    #txt
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
	FileName = input("Enter file name to save as: ")    #.txt
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
	print("Adding your preset...")
	time.sleep(2)
	with open("settings.json") as json_file:
		json_decoded = json.load(json_file)

	json_decoded[preset] = NumOfTimes

	with open("settings.json", 'w') as json_file:
		json.dump(json_decoded, json_file)
	print("Preset Added!")

elif Type == "about":
	print("""\n
	███████╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗██╗░█████╗░███╗░░██╗
	██╔════╝████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
	█████╗░░██╔██╗██║██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║██║░░██║██╔██╗██║
	██╔══╝░░██║╚████║██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║██║░░██║██║╚████║
	███████╗██║░╚███║╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░██║╚█████╔╝██║░╚███║
	╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝v1.8
	
	Hi I am Siddharth
	
	## Instructions to start
	
	For windows users Run the batch file (.bat)
	For Mac and Linix users Open the `scripts\Main.py` With Python Installed [Python Website](https://www.python.org/)
	
	## App Instructions
	 - Type "e" in the field given to encrypt
	 - Type the number of time for the Program to encrypt the sentence
	 - Type the Phrase to be encrypted
	 - You Recive a Scrambled Word
	
	 - The Number and scrambled Phrase must be given to the Reciver
	 - The Reciver Must Type "d" to Decrypt the word Given
	 - The Reciver Must Type in the number used for encrypting the word (Number of time the program must encrypt used before)
	 - Then the sentence given
	 - The program will Show the sentence
	
	Note that the program for now only encrypts a-z and 0-9 other symbols wont be encrypted and will show as it is
	
	This software is and always will be free, but if you support the development, it will be largely appreciated:
	
	Ethererm Address : 0x448A558863DBA1e3392Cd0a80ea497c06821d2aA (I use MetaMask hence the repeted address)
	 Binance Address : 0x448A558863DBA1e3392Cd0a80ea497c06821d2aA
	 Polygon Address : 0x448A558863DBA1e3392Cd0a80ea497c06821d2aA
	 Bitcoin Address : 177fzZh3t3cPccAeX4bTpVW5tAEkzZSB7V
	    Doge Address : DNTouZp7GsbqNbA7xjrqJwDvfD1Y9qHPDv
	This is Made By Siddharth Of King siddhu (https://www.youtube.com/channel/UCm-Tcpc9zDONytmwS1Y91-Q)""")

elif Type =="help":
	print("""
	"e" in the first field encrypts the given text
	"d" in the first field Decrypts the encrypted text
	"e -s" in the first field Saves the encrypted text in the File name specified
	"d -r" in the first field can help you to decrypt  files sent by the user
	"e -r -s" in the first field Encrypts the text file given and save it in enc format
	"d -r -s" in the first field can help you to decrypt txt files sent by the user and save it
	"add" to add a preset for ease.
	"TriggerOriginal" can be used to check original message
	"about" for info 
	""")

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




elif Type == "eb -r -s":
	print("\n")
	for a in os.listdir():
		print(a)
	print("\n")
	FileName = input("Enter Encrypted file name without extension: ")    #enc
	ext = input("File extension: ")
	SaveFile = input("File name to Save as: ")    #txt
	File = (SaveFile + ext)              #txt
	File = open(File, "rb")                #txt
	encrypt = File.read()                   #txt
	#encrypt = encrypt.lower()               #txt
	print("\nDecrypting your message...\n")
	print("Since I am Encrypting a file, I am taking time...")
	for index in range(NumOfTimes):
		encrypt = Encrypt(encrypt)
	SaveFile = (SaveFile + ".txt")
	text = open(SaveFile, "a")
	text.write(encrypt)
	text.close()
	print()
	print("Output is in the folder of the program" , SaveFile)

elif Type == "db -r -s":
	print("\n")
	for a in os.listdir():
		print(a)
	print("\n")
	FileName = input("File to Decrypt")    #enc
	ext = input("File extension to save as: ")
	SaveFile = input("File name to Save as: ")    #txt
	Fileenc = (SaveFile + ".enc")         #.enc
	Fileenc = open(Fileenc, "r+")            #.enc
	encrypt = Fileenc.read()              #.enc
	#encrypt = encrypt.lower()          #.enc
	print("\nDecrypting your message...\n")
	print("Since I am Decrypting a file, I am taking time...")
	for index in range(NumOfTimes):
		encrypt = Decrypt(encrypt)
	text = open(FileName + ".txt", "wb")   
	text.write(encrypt)
	text.close()
	print()
	print("Output is in the folder of the program" , FileName)




else:
	print("ERROR WRONG METHOD GIVEN")


Exit = input("Press Enter to exit...")

