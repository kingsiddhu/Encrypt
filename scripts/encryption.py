#Encrypton by siddharth
##V2
##qwertyuiopasdfghjklzxcvbnm1234567890`-=[];',./ QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()~_+{}|:"<>?
##`1qaz2wsx3edc4rfv5tgb6yhn7ujm 8ik,9ol.0p;/-['=]~!QAZ@WSX#EDC$RFV%TGB^YHN&UJM*IK<(OL>)P:?_{"+}|
def Encrypt(phrase, NumOfTimes=1):
    """
    This Encrypts your phrase
    """
    before = r"""qwertyuiopasdfghjklzxcvbnm1234567890`-=]£;',./ QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()~_+{}|:"<>?"""
    afters = r"""ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+`1234567890-=ABCDEFGHIJKLMNOPQRSTUVWXYZ{}|:"<>? ,./;'[]"""
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
    afters = r"""ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+`1234567890-=ABCDEFGHIJKLMNOPQRSTUVWXYZ{}|:"<>? ,./;'[]"""
    encrypt = ""
    for en in phrase:
        if en == "\n":
            encrypt = encrypt + "\n"
        elif before.find(en) == -1:
            encrypt = encrypt + en
        else:
            encrypt = encrypt + before[afters.find(en)]
    return encrypt

