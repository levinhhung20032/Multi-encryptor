import math
import numpy as np
from numpy import array, zeros
from numpy.linalg import det

from Model import DAO


def minor(A, i, j):
    A = array(A)
    n = len(A)
    minorize = zeros((n - 1, n - 1), dtype=int)
    p = 0
    for s in range(0, n - 1):
        if p == i:
            p = p + 1
        q = 0
        for t in range(0, n - 1):
            if q == j:
                q = q + 1
            minorize[s][t] = A[p][q]
            q = q + 1
        p = p + 1
    return minorize


def modInverse(a, m):
    if math.gcd(a, m) != 1 or (m == 1):
        return
    m0 = m
    y = 0
    x = 1
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x = x + m0
    return x


def matrixInverse_modn(A, m):
    if m <= 1:
        print("Modulo n must be greater or equal 2 !")
    n = len(A)
    for i in range(0, n):
        for j in range(0, n):
            A[i][j] = (A[i][j] % m)
    d = int(round(
        det(A)) % m)
    if math.gcd(d, m) != 1:
        print("Inverse modulo " + str(m) + " does not exist because matrix A is singular!")
        return None
    adj = zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            M = minor(A, i, j)
            adj[j][i] = int((round(det(M)) % m))
            if (i + 1 + j + 1) % 2 == 1:
                adj[j][i] = (-1 * adj[j][i]) % m
    return (modInverse(d, m) * adj) % m


def Encrypt(k):
    m = math.isqrt(len(k))
    k = np.array(k).reshape((m, m))

    i = DAO.GetText()
    if len(i) % m != 0:
        in_matrix = np.full(fill_value=32, shape=((len(i) // m) + 1, m), dtype=int)
    else:
        in_matrix = np.full(fill_value=32, shape=((len(i) // m), m), dtype=int)
    for j in range(len(i)):
        in_matrix[j // m][j % m] = ord(i[j])
    out_matrix = np.dot(in_matrix, k).flatten() % 128
    output = "".join(chr(s) for s in out_matrix)
    output = DAO.txt_bin(output)
    return output


def Decrypt(k):
    m = math.isqrt(len(k))
    k = np.array(k).reshape((m, m))

    k = matrixInverse_modn(k, 128)

    i = DAO.GetCrypt()
    if len(i) % m != 0:
        in_matrix = np.full(fill_value=32, shape=((len(i) // m) + 1, m), dtype=int)
    else:
        in_matrix = np.full(fill_value=32, shape=((len(i) // m), m), dtype=int)
    for j in range(len(i)):
        in_matrix[j // m][j % m] = ord(i[j])
    out_matrix = np.dot(in_matrix, k).flatten() % 128
    output = "".join(chr(s) for s in out_matrix)
    output = DAO.txt_bin(output)
    return output
