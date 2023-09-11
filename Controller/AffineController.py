from Model import DAO

x, y = 0, 1


def GCDExtended(a, b):
    global x, y

    if a == 0:
        x = 0
        y = 1
        return b
    gcd = GCDExtended(b % a, a)
    x1 = x
    y1 = y

    x = y1 - (b // a) * x1
    y = x1
    return gcd


def ModuloInverse(a, m):
    gcd = GCDExtended(a, m)
    inversed = x % m
    return inversed


def Encrypt(k):
    output = ""
    for i in DAO.GetText():
        output += DAO.txt_bin(chr((ord(i) * k[0] + k[1]) % 128))
    return output


def Decrypt(k):
    output = ""
    a = ModuloInverse(k[0], 128)
    for i in DAO.GetCrypt():
        output += DAO.txt_bin(chr((a * (ord(i) - k[1])) % 128))
    return output
