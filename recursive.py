"""
Recursive algorithm to multiply two square matrices. 8 recursive loops.
O(n^3).
"""

def recursive_mtx_multip(mtx1, mtx2):
    """
    multiplies two square matrices of equal size, n x n, where n is multiple of 2.
    :return product_mtx of size n x n
    """
    n = len(mtx1)
    half_n = n//2
    #Base case - scalar multiplication of two 1 x 1 matrices
    if n == 1:
        return(mtx1[0][0] * mtx2[0][0])

    #Recursive steps
    A = [[mtx1[j][i] for i in range(half_n)] for j in range(half_n)]
    B = [[mtx1[j][i] for i in range(half_n, n)] for j in range(half_n)]
    C = [[mtx1[j][i] for i in range(half_n)] for j in range(half_n, n)]
    D = [[mtx1[j][i] for i in range(half_n, n)] for j in range(half_n, n)]
    E = [[mtx2[j][i] for i in range(half_n)] for j in range(half_n)]
    F = [[mtx2[j][i] for i in range(half_n, n)] for j in range(half_n)]
    G = [[mtx2[j][i] for i in range(half_n)] for j in range(half_n, n)]
    H = [[mtx2[j][i] for i in range(half_n, n)] for j in range(half_n, n)]

    LU = matrix_addition(recursive_mtx_multip(A,E), recursive_mtx_multip(B,G))
    RU = matrix_addition(recursive_mtx_multip(A,F), recursive_mtx_multip(B,H))
    LL = matrix_addition(recursive_mtx_multip(C,E), recursive_mtx_multip(D,G))
    RL = matrix_addition(recursive_mtx_multip(C,F), recursive_mtx_multip(D,H))

    result = [[0 for i in range(n)] for j in range(n)]
    if n > 2:
        for i in range(half_n):
            for j in range(half_n):
                result[i][j] = LU[i][j]
                result[i + half_n][j] = LL[i][j]
                result[i][j + half_n] = RU[i][j]
                result[i + half_n][j + half_n] = RL[i][j]
        return result
    else:
        return [[LU, RU], [LL, RL]]


def matrix_addition(mtx1, mtx2):
    """Adds two square matrices."""
    if type(mtx1) == int:
        return mtx1 + mtx2
    else:
        n = len(mtx1)
        return [[mtx1[j][i] + mtx2[j][i] for i in range(n)] for j in range(n)]


def print_matrix(matrix):
    """prints any matrix"""
    print("_____________")
    for row in range(len(matrix)):
        print("")
        for col in range(len(matrix[0])):
            print(matrix[row][col], end= " ")
        print("")

print("___________________________________")

m1 = [(1,2,3,4),
      (5,6,7,8),
      (9,10,11,12),
      (13,14,15,16)]
m2 = [(21,22,23,24),
      (25,26,27,28),
      (29,30,31,32),
      (33,34,35,36)]

n1 = ((1,2),
      (3,4))
n2 = ((6,7),
      (8,9))
print_matrix(recursive_mtx_multip(n1,n2))

