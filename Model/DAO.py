def SetText(s):
    f = open("Data/text.txt", "w")
    f.write(s)
    f.close()


def SetCrypt(s):
    f = open("Data/crypt.txt", "w")
    f.write(s)
    f.close()


def GetText():
    f = open("Data/text.txt", "r")
    s = f.read()
    f.close()
    return s


def GetCrypt():
    f = open("Data/crypt.txt", "r")
    s = f.read()
    f.close()
    return s
