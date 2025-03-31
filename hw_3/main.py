from matrix import Matrix 
import numpy as np


if __name__ == "__main__":

    #task1
    np.random.seed(0)
    m1 = np.random.randint(0, 10, (10, 10))
    m2 = np.random.randint(0, 10, (10, 10))
    
    mat1 = Matrix(m1.tolist())
    mat2 = Matrix(m1.tolist())
    mat1 = mat1 + mat2
    mat1.to_file("artifacts/matrix+.txt")

    mat1 = Matrix(m1.tolist())
    mat1 = mat1 + mat2
    mat1.to_file("artifacts/matrix*.txt")

    mat1 = Matrix(m1.tolist())
    mat1 = mat1 @ mat2
    mat1.to_file("artifacts/matrix@.txt")

    #task2

    mat1 = Matrix(m1.tolist())
    mat1 = mat1 - mat2
    mat1.to_file("artifacts/matrix-.txt")

    mat1 = Matrix(m1.tolist())
    mat1 -= mat2
    mat1.to_file("artifacts/matrix-=.txt")

    mat1 = Matrix(m1.tolist())
    mat1 += mat2
    mat1.to_file("artifacts/matrix+=.txt")

    mat1 = Matrix(m1.tolist())
    mat1 *= mat2
    mat1.to_file("artifacts/matrix*=.txt")

    mat1 = Matrix(m1.tolist())
    mat1 @= mat2
    mat1.to_file("artifacts/matrix@=.txt")

    mat1 = Matrix(m1.tolist())
    print(mat1) 

    #task 3
    md = Matrix([[5, 6], [7, 8]]) # sum=26, rows=2 → hash=28
    mb = Matrix([[5, 6], [7, 8]]) # sum=26, rows=2 → hash=28
    ma = Matrix([[0, 3], [2, 2]])  # sum=7, rows=2 → hash=9
    mc = Matrix([[1, 1], [2, 3]])  # sum=7, rows=2 → hash=9

    ma.to_file("artifacts/A.txt")
    mb.to_file("artifacts/B.txt")
    mc.to_file("artifacts/C.txt")
    md.to_file("artifacts/.txt")
    ma = ma @ mb
    mc = mc @ md

    ma.to_file("artifacts/AB.txt")
    mc.to_file("artifacts/CD.txt")

    
