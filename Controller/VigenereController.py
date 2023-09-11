from Model import DAO


def Encrypt(k):
    output = ""
    count = 0
    for i in DAO.GetText():
        output += DAO.txt_bin(chr((ord(i) + ord(k[count % len(k)])) % 128))
        count += 1
    return output


def Decrypt(k):
    output = ""
    count = 0
    for i in DAO.GetCrypt():
        output += DAO.txt_bin(chr((ord(i) - ord(k[count % len(k)])) % 128))
        count += 1
    return output
