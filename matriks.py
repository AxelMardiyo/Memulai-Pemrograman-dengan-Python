matriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matriks)
# membuat matriks pake list tidak efektif, karena memakan banyak memori
# jadi pake numpy

import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriks)

# Deklarasi matriks langsung dengan nilainya
matriks = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]

print(matriks)

# Deklarasi dengan nilai default
matriks = [[0 for j in range(4)] for i in range(3)]

print(matriks)


# Mengakses elemen matriks
var_mat = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

print(var_mat[2][1])  # [baris][kolom]

# operasi matriks
# Perkalian dengan skalar 2
var_mat = [[5, 0], [1, -2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
    for j in range(len(var_mat[0])):
        def_mat[i][j] = var_mat[i][j] * 2

print(def_mat)

# kalo pake numpy
var_mat = numpy.array([[5, 0], [1, -2]])
def_mat1 = var_mat * 2
print(def_mat1)
