"""
Strassen recursive algorithm to multiply 2 square matrices 7 recursive loops.
"""

def strassen_mtx_multip(mtx1, mtx2):
    """
    multiplies two square matrices, n x n, where n is a power of 2
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

    p1 = strassen_mtx_multip(A, matrix_subtraction(F, H))
    p2 = strassen_mtx_multip(matrix_addition(A, B), H)
    p3 = strassen_mtx_multip(matrix_addition(C, D), E)
    p4 = strassen_mtx_multip(D, matrix_subtraction(G, E))
    p5 = strassen_mtx_multip(matrix_addition(A, D), matrix_addition(E, H))
    p6 = strassen_mtx_multip(matrix_subtraction(B, D), matrix_addition(G, H))
    p7 = strassen_mtx_multip(matrix_subtraction(A, C), matrix_addition(E, F))

    LU = matrix_addition(matrix_subtraction(matrix_addition(p5, p4), p2), p6)
    LL = matrix_addition(p3, p4)
    RU = matrix_addition(p1, p2)
    RL = matrix_subtraction(matrix_subtraction(matrix_addition(p1, p5), p3), p7)

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

def matrix_subtraction(mtx1, mtx2):
    """Subtracts two square matrices."""
    if type(mtx1) == int:
        return mtx1 - mtx2
    else:
        n = len(mtx1)
        return [[mtx1[j][i] - mtx2[j][i] for i in range(n)] for j in range(n)]

def print_matrix(matrix):
    """prints any matrix"""
    print("_____________")
    for row in range(len(matrix)):
        print("")
        for col in range(len(matrix[0])):
            print(matrix[row][col], end= " ")
        print("")

print("_________________________________")
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


print_matrix(strassen_mtx_multip(m1,m2))

