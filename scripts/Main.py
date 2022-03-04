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

print("Use This Program To Encrypt or Decrypt Text \nThanks for useing this Program All writen by Siddharth\nThe Encryption Number Must be Informed to the Reciver to Decrypt")
print("")
#Inputs

Type = input("Type e to encrypt, d to decrypt and info for info")
NumOfTimes = int(input("Enter The Encryption Number "))
PhraseToEncrypt = input("Phase to Encrypt ")
PhraseToEncrypt = PhraseToEncrypt.lower()

#Main
if Type == "e":
	for index in range(NumOfTimes):
		PhraseToEncrypt = Encrypt(PhraseToEncrypt)

elif Type == "d":
	for index in range(NumOfTimes):
		PhraseToEncrypt = Decrypt(PhraseToEncrypt)

elif Type == "about":
	print("This is Made By Siddharth Of King siddhu (https://www.youtube.com/channel/UCm-Tcpc9zDONytmwS1Y91-Q)")

else:
	print("ERROR WRONG METHOD GIVEN")



print(PhraseToEncrypt)




Exit = input("")
