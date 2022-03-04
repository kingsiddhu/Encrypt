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