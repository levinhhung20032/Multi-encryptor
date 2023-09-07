from Model import DAO


def Encrypt(k):
    output = ""
    for i in DAO.GetText():
        if ord(i) != 10:
            output += chr((ord(i) + k - 32) % 95 + 32)
        else:
            output += chr(10)
    return output


def Decrypt(k):
    output = ""
    for i in DAO.GetCrypt():
        if ord(i) != 10:
            output += chr((ord(i) - k - 32) % 95 + 32)
        else:
            output += chr(10)
    return output
