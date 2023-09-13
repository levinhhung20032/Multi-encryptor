from Model import DAO


def Encrypt(k):
    s = DAO.GetText()
    dicts = []
    for i in range(len(s)):
        dicts.append(i)
    EncryptDict = dict(zip(dicts, k))
    output = ""
    for i in range(len(s)):
        output += DAO.txt_bin(s[EncryptDict[i]])
    return output


def Decrypt(k):
    s = DAO.GetCrypt()
    dicts = []
    for i in range(len(s)):
        dicts.append(i)
    DecryptDict = dict(zip(k, dicts))
    output = ""
    for i in range(len(s)):
        output += DAO.txt_bin(s[DecryptDict[i]])
    return output
