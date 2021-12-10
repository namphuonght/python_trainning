"""
Test
==========

Build test functions for Matrix class
"""


# =============================================================================


__author__ = 'Tran Nam Phuong'
__email__ = 'trannamphuong2k@gmail.com'
__date__ = '2021/12/09'
__status__ = 'development'


# =============================================================================


from matrix import Matrix


# =============================================================================


def cal_Add(mat1, mat2):
    ret = Matrix(mat1.m, mat1.n)
    for i in range(mat1.m):
        row = [sum(item) for item in zip(mat1[i], mat2[i])]
        ret[i] = row
    
    return ret


# =============================================================================


def cal_Sub(mat1, mat2):
    ret = Matrix(mat1.m, mat2.n)
    for i in range(mat1.m):
        row = [item[0]-item[1] for item in zip(mat1[i], mat2[i])]
        ret[i] = row

    return ret


# =============================================================================


def cal_Mul(mat1, mat2):
    mat2_t = mat2.getTranspose()
    mul_mat = Matrix(mat1.m, mat2.n)

    for x in range(mat1.m):
        for y in range(mat2_t.m):
            mul_mat[x][y] = sum([item[0]*item[1] for item in zip(mat1[x], mat2_t[y])])

    return mul_mat


# =============================================================================


def testAdd():
    mat1 = Matrix.makeRandom(3,4)
    mat2 = Matrix.makeRandom(3,4)
    assert mat1 + mat2 == cal_Add(mat1, mat2)



# =============================================================================


def testSub():
    mat1 = Matrix.makeRandom(3,4)
    mat2 = Matrix.makeRandom(3,4)
    assert mat1 - mat2 == cal_Sub(mat1, mat2)


# =============================================================================


def testMul():
    mat1 = Matrix.makeRandom(3,4)
    mat2 = Matrix.makeRandom(4,3)
    assert mat1 * mat2 == cal_Mul(mat1, mat2)


