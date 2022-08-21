#Encrypton by siddharth
##V2
##qwertyuiopasdfghjklzxcvbnm1234567890`-=]£;',./ QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()~_+{}|:"<>?
##aM6 ABCDE=N[]£127890-defghijklm3VWXYxyz,"{nop4.~!@#$%^Z<>?:5}|_+tbcFGHIJKLuvw&*()OPQRSTUqrs/;'
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

