import math

from Model import DAO


def Encrypt(k):
    m = math.isqrt(k)
    output = ""
    for i in DAO.GetText():
        if 32 <= ord(i) <= 126:
            output += chr((ord(i) + k - 32) % 95 + 32)
        else:
            output += i
    return output


def Decrypt(k):
    output = ""
    for i in DAO.GetCrypt():
        if 32 <= ord(i) <= 126:
            output += chr((ord(i) - k - 32) % 95 + 32)
        else:
            output += i
    return output
