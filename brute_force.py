"""
Brute force iterative matrix multiplication O(n^3).
"""
def square_mtx_multip(mtx1, mtx2):
    """
    multiplies two square matrices of equal size, n x n
    :return product_mtx: n x n matrix
    """
    n = len(mtx1)
    product_mtx = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            product_mtx[i][j] = sum([mtx1[i][k] * mtx2[k][j] for k in range(n)])
    return product_mtx

def mtx_multip(mtx1, mtx2):
    """
    Multiplies 2 non-sqaure matrices
    :param mtx1: matrix of size m x n
    :param mtx2: matrix of size n x m
    :return: product matrix m x m (if m > n), or n x n (if n > m)
    """
    longer_side = max(len(mtx1), len(mtx1[0]))
    shorter_side = min(len(mtx1), len(mtx1[0]))
    product_mtx = [[0 for i in range(longer_side)] for j in range(longer_side)]
    for i in range(longer_side):
        for j in range(longer_side):
            product_mtx[i][j] = sum([mtx1[i][k] * mtx2[k][j] for k in range(shorter_side)])
    return product_mtx

def print_matrix(matrix):
    """prints any matrix"""
    print("_____________")
    for row in range(len(matrix)):
        print("")
        for col in range(len(matrix[0])):
            print(matrix[row][col], end= " ")
        print("")

print("___________________________________")
m1 = ((2, 3),
      (-1, -2),
      (3, 4))
m2 = ((4, 6, 1),
      (-6, 3, 2))

print_matrix(mtx_multip(m1, m2))
