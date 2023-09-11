import numpy as np


def SetText(s):
    f = open("Data/text.txt", "w")
    f.write(txt_bin(s))
    f.close()


def SetCrypt(s):
    f = open("Data/crypt.txt", "w")
    f.write(txt_bin(s))
    f.close()


def GetText():
    f = open("Data/text.txt", "r")
    s = bin_txt(f.read())
    f.close()
    return s


def GetBinText():
    f = open("Data/text.txt", "r")
    s = f.read()
    f.close()
    return s


def GetCrypt():
    f = open("Data/crypt.txt", "r")
    s = bin_txt(f.read())
    f.close()
    return s


def GetBinCrypt():
    f = open("Data/crypt.txt", "r")
    s = f.read()
    f.close()
    return s


def txt_bin(s):
    output = ""
    for i in s:
        output += bin(ord(i)).replace("0b", "").zfill(8)
    return output


def bin_txt(s):
    char = np.array(list(s)).reshape((len(s) // 8, 8)).tolist()
    for i in range(len(char)):
        char[i] = "".join(char[i])
        char[i] = chr(int(char[i], 2))
    return "".join(char)
