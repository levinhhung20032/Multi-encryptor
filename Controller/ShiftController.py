from Model import DAO


def Encrypt(k):
    output = ""
    s = DAO.GetBinText()
    s = [s[8 * i:8 * i + 8] for i in range(len(s) // 8)]
    for i in s:
        output += bin((int(i, 2) + k) % 128).replace("0b", "").zfill(8)
    return output


def Decrypt(k):
    output = ""
    s = DAO.GetBinCrypt()
    s = [s[8 * i:8 * i + 8] for i in range(len(s) // 8)]
    for i in s:
        output += bin((int(i, 2) - k) % 128).replace("0b", "").zfill(8)
    return output
