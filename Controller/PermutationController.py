from Model import DAO


def Encrypt(k):
    alphabet = ""
    for i in range(95):
        alphabet += chr(32 + i)
    EncryptDict = dict(zip(alphabet, k))
    output = ""
    for i in DAO.GetText():
        if 32 <= ord(i) <= 126:
            output += DAO.txt_bin(EncryptDict[i])
        else:
            output += DAO.txt_bin(i)
    return output


def Decrypt(k):
    alphabet = ""
    for i in range(95):
        alphabet += chr(32 + i)
    DecryptDict = dict(zip(k, alphabet))
    output = ""
    for i in DAO.GetCrypt():
        if 32 <= ord(i) <= 126:
            output += DAO.txt_bin(DecryptDict[i])
        else:
            output += DAO.txt_bin(i)
    return output
