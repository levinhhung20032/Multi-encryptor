from Model import DAO


def Encrypt(k):
    alphabet = ""
    for i in range(95):
        alphabet += chr(32 + i)
    EncryptDict = dict(zip(alphabet, k))
    output = ""
    for i in DAO.GetText():
        if 32 <= ord(i) <= 126:
            output += EncryptDict[i]
        else:
            output += i
    return output


def Decrypt(k):
    alphabet = ""
    for i in range(95):
        alphabet += chr(32 + i)
    DecryptDict = dict(zip(k, alphabet))
    output = ""
    for i in DAO.GetCrypt():
        if 32 <= ord(i) <= 126:
            output += DecryptDict[i]
        else:
            output += i
    return output
