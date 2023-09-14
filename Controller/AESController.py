from Model import DAO
import numpy as np

sub = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
       ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
       ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
       ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
       ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
       ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
       ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
       ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
       ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
       ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
       ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
       ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
       ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
       ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
       ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
       ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]

inv_sub = [['52', '09', '6a', 'd5', '30', '36', 'a5', '38', 'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb'],
           ['7c', 'e3', '39', '82', '9b', '2f', 'ff', '87', '34', '8e', '43', '44', 'c4', 'de', 'e9', 'cb'],
           ['54', '7b', '94', '32', 'a6', 'c2', '23', '3d', 'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e'],
           ['08', '2e', 'a1', '66', '28', 'd9', '24', 'b2', '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25'],
           ['72', 'f8', 'f6', '64', '86', '68', '98', '16', 'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92'],
           ['6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da', '5e', '15', '46', '57', 'a7', '8d', '9d', '84'],
           ['90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a', 'f7', 'e4', '58', '05', 'b8', 'b3', '45', '06'],
           ['d0', '2c', '1e', '8f', 'ca', '3f', '0f', '02', 'c1', 'af', 'bd', '03', '01', '13', '8a', '6b'],
           ['3a', '91', '11', '41', '4f', '67', 'dc', 'ea', '97', 'f2', 'cf', 'ce', 'f0', 'b4', 'e6', '73'],
           ['96', 'ac', '74', '22', 'e7', 'ad', '35', '85', 'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e'],
           ['47', 'f1', '1a', '71', '1d', '29', 'c5', '89', '6f', 'b7', '62', '0e', 'aa', '18', 'be', '1b'],
           ['fc', '56', '3e', '4b', 'c6', 'd2', '79', '20', '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4'],
           ['1f', 'dd', 'a8', '33', '88', '07', 'c7', '31', 'b1', '12', '10', '59', '27', '80', 'ec', '5f'],
           ['60', '51', '7f', 'a9', '19', 'b5', '4a', '0d', '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef'],
           ['a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0', 'c8', 'eb', 'bb', '3c', '83', '53', '99', '61'],
           ['17', '2b', '04', '7e', 'ba', '77', 'd6', '26', 'e1', '69', '14', '63', '55', '21', '0c', '7d']]

rcon = [['01', '00', '00', '00'], ['02', '00', '00', '00'], ['04', '00', '00', '00'], ['08', '00', '00', '00'],
        ['10', '00', '00', '00'], ['20', '00', '00', '00'], ['40', '00', '00', '00'], ['80', '00', '00', '00'],
        ['1b', '00', '00', '00'], ['36', '00', '00', '00'], ['6C', '00', '00', '00'], ['D8', '00', '00', '00'],
        ['AB', '00', '00', '00'], ['4D', '00', '00', '00'], ['9A', '00', '00', '00'], ['2F', '00', '00', '00'],
        ['5E', '00', '00', '00'], ['BC', '00', '00', '00'], ['63', '00', '00', '00'], ['C6', '00', '00', '00'],
        ['97', '00', '00', '00'], ['35', '00', '00', '00'], ['6A', '00', '00', '00'], ['D4', '00', '00', '00'],
        ['B3', '00', '00', '00'], ['7D', '00', '00', '00'], ['FA', '00', '00', '00'], ['EF', '00', '00', '00'],
        ['c5', '00', '00', '00']]

c = [['02', '03', '01', '01'],
     ['01', '02', '03', '01'],
     ['01', '01', '02', '03'],
     ['03', '01', '01', '02']]

c_1 = [['0E', '0B', '0D', '09'],
       ['09', '0E', '0B', '0D'],
       ['0D', '09', '0E', '0B'],
       ['0B', '0D', '09', '0E']]

relate = {128: 10,
          192: 12,
          256: 14}


def leftshift(a):
    temp = [a[1], a[2], a[3], a[0]]
    return temp


def rightshift(a):
    temp = [a[3], a[0], a[1], a[2]]
    return temp


def block_state(block):
    state = np.array(block)
    state = state.reshape((4, 4))
    state = state.transpose()
    return state


def state_block(state):
    block = np.array(state)
    block = block.transpose()
    block = block.flatten()
    return block


def Sub(code):
    output = []
    for i in code:
        output.append(sub[int(i[0], 16)][int(i[1], 16)])
    return output


def InvSub(code):
    output = []
    for i in code:
        output.append(inv_sub[int(i[0], 16)][int(i[1], 16)])
    return output


def temp_word(word, step):
    word = leftshift(word)
    word = xor(Sub(word), rcon[step])
    return word


def mini_key(k, mode):
    k = [k[2 * i: 2 * i + 2] for i in range(len(k) // 2)]
    w = [k[4 * i: 4 * i + 4] for i in range(len(k) // 4)]
    count = 3
    for i in w:
        if (count + 1) % (mode // 32) == 0:
            w.append(xor(i, temp_word(w[count], count // (mode // 32))))
        else:
            w.append(xor(i, w[count]))
        count += 1
        if count == 4 * relate[mode] + 3:
            break
    w = [w[(mode // 32) * i] + w[(mode // 32) * i + 1] + w[(mode // 32) * i + 2] + w[(mode // 32) * i + 3] for i in
         range(len(w) // (mode // 32))]
    return w


def ShiftRows(block):
    state = block_state(block)
    output = []
    count = 0
    for i in state:
        temp = i.tolist()
        for j in range(count):
            temp = leftshift(temp)
        output.append(temp)
        count += 1
    return state_block(output)


def InvShiftRows(block):
    state = block_state(block)
    output = []
    count = 0
    for i in state:
        temp = i.tolist()
        for j in range(count):
            temp = rightshift(temp)
        output.append(temp)
        count += 1
    return state_block(output)


def Polynomial(a, b):
    if b == 1:
        return a
    if b == 2:
        tmp = (a << 1) & 0xff
        return tmp if a < 128 else tmp ^ 0x1b
    if b == 3:
        return Polynomial(a, 2) ^ a
    if b == 9:
        return Polynomial(Polynomial(Polynomial(a, 2), 2), 2) ^ a
    if b == 11:
        return Polynomial(Polynomial(Polynomial(a, 2), 2), 2) ^ Polynomial(a, 3)
    if b == 13:
        return Polynomial(Polynomial(Polynomial(a, 2), 2), 2) ^ Polynomial(Polynomial(a, 2), 2) ^ a
    if b == 14:
        return Polynomial(Polynomial(Polynomial(a, 2), 2), 2) ^ Polynomial(Polynomial(a, 2), 2) ^ Polynomial(a, 2)


def MixColumns(block):
    state = block_state(block)
    output = np.zeros(shape=(4, 4), dtype=int)
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if k == 0:
                    output[i][j] = Polynomial(int(state[:, j][k], 16), int(c[i][k], 16))
                else:
                    output[i][j] ^= Polynomial(int(state[:, j][k], 16), int(c[i][k], 16))
    return state_block(int_hex_matrix(output))


def InvMixColumns(block):
    state = block_state(block)
    output = np.zeros(shape=(4, 4), dtype=int)
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if k == 0:
                    output[i][j] = Polynomial(int(state[:, j][k], 16), int(c_1[i][k], 16))
                else:
                    output[i][j] ^= Polynomial(int(state[:, j][k], 16), int(c_1[i][k], 16))
    return state_block(int_hex_matrix(output))


def hex_bin(hexcode):
    code = ""
    for i in hexcode:
        code += bin(int(i, 16)).replace("0b", "").zfill(4)
    return code


def bin_hex(code):
    output = ""
    code = [code[4 * i:4 * i + 4] for i in range(len(code) // 4)]
    for i in code:
        output += hex(int(i, 2)).replace("0x", "").upper()
    return output


def hex_int_matrix(matrix):
    output = []
    for i in matrix:
        for j in i:
            output.append(int(j, 16))
    output = np.array(output).reshape((4, 4))
    return output


def int_hex_matrix(matrix):
    output = []
    for i in matrix:
        for j in i:
            output.append(hex(j).replace("0x", "").zfill(2))
    output = np.array(output).reshape((4, 4))
    return output


def xor(a, b):
    result = []
    for i in range(len(a)):
        result.append(hex(int(a[i], 16) ^ int(b[i], 16)).replace("0x", "").zfill(2))
    return result


def Encrypt(k, mode):
    key = mini_key(k, mode)
    s = DAO.GetBinText()
    s = bin_hex(s)
    output = []
    while len(s) % 32 != 0:
        s += "20"
    s = [s[2 * i: 2 * i + 2] for i in range(len(s) // 2)]
    s = [s[16 * i: 16 * i + 16] for i in range(len(s) // 16)]
    for para in s:
        output_i = xor(para, key[0])
        for i in range(relate[mode]):
            output_i = Sub(output_i)
            output_i = ShiftRows(output_i)
            if i != 9:
                output_i = MixColumns(output_i)
            output_i = xor(output_i, key[i + 1])
        output.append(output_i)
    for i in range(len(output)):
        output[i] = "".join(output[i])
    output = "".join(output)
    return hex_bin(output)


def Decrypt(k, mode):
    key = mini_key(k, mode)
    key.reverse()
    s = DAO.GetBinCrypt()
    s = bin_hex(s)
    output = []
    while len(s) % 32 != 0:
        s += "20"
    s = [s[2 * i: 2 * i + 2] for i in range(len(s) // 2)]
    s = [s[16 * i: 16 * i + 16] for i in range(len(s) // 16)]
    for para in s:
        output_i = xor(para, key[0])
        for i in range(relate[mode]):
            output_i = InvShiftRows(output_i)
            output_i = InvSub(output_i)
            output_i = xor(output_i, key[i + 1])
            if i != 9:
                output_i = InvMixColumns(output_i)
        output.append(output_i)
    for i in range(len(output)):
        output[i] = "".join(output[i])
    output = "".join(output)
    return hex_bin(output)
