from Model import DAO


def Encrypt(k):
    output = ""
    count = 0
    for i in DAO.GetText():
        if 32 <= ord(i) <= 126:
            output += chr(((ord(i) - 32) + (ord(k[count % len(k)]) - 32)) % 95 + 32)
            count += 1
        else:
            output += i
    return output


def Decrypt(k):
    output = ""
    count = 0
    for i in DAO.GetCrypt():
        if 32 <= ord(i) <= 126:
            output += chr(((ord(i) - 32) - (ord(k[count % len(k)]) - 32)) % 95 + 32)
            count += 1
        else:
            output += i
    return output

