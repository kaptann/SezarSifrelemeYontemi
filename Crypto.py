def crp(text, scrl):
    pasw = ""

    for each in text:
        pasw = pasw+chr(ord(each) + scrl)

    return  print("Olusturulan Sifre :", pasw)

def dcrp(ppsw, scrl):
    text = ""

    for each in ppsw:
        text = text+chr(ord(each) - scrl)

    return  print("Cozulen Sifre :", text)