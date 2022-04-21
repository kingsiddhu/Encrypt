#Encrypton

def Encrypt(phrase):
	encrypt = ""
	for en in phrase:
		slash = ("\\")
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
		elif en in "\\":
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
			encrypt = encrypt + slash
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



#DeCryption


def Decrypt(phrase):
	slash = (r"\\")
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
			encrypt = encrypt + slash
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
		elif en in slash:
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