"""
Calculator
==========

Build support functions for Matrix operations
"""


# =============================================================================

__auth__ = 'Tran Nam Phuong'
__email__ = 'trannamphuong2k@gmail.com'
__date__ = '2021/12/10'
__status__ = 'development'


# =============================================================================


import math
import random


# =============================================================================


class MatrixError(Exception):
    """ An exception class for Matrix """
    pass


class Matrix(object):
    """ Create a matrix"""
    def __init__(self, m, n, init = True):
        if init:
            self.rows = [[0]*n for _ in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n


# =============================================================================


    def __getitem__(self, idx):
        return self.rows[idx]


# =============================================================================


    def __setitem__(self, idx, item):
        self.rows[idx] = item


# =============================================================================


    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + "\n"


# =============================================================================


    def __repr__(self):
        s = str(self.rows)
        rank = str(self.getRank())
        rep = "Matrix: \"%s\", rank: \"%s\"" %(s, rank)
        return rep  


# =============================================================================


    def reset(self):
        """Reset the matrix data"""
        self.rows = [[] for _ in range(self.m)]

    
# =============================================================================


    def transpose(self):
        """Transpose the matrix. Changes the current matrix"""

        self.m, self.n = self.n, self.m
        self.rows = [list(item) for item in zip(*self.rows)]


# =============================================================================


    def getTranspose(self):
        """Return a transpose of the matrix without modifying the matrix itself"""
        m, n = self.n, self.m
        mat = Matrix(m, n)
        mat.rows = [list(item) for item in zip(*self.rows)]

        return mat


# =============================================================================


    def getRank(self):
        return (self.m, self.n)


# =============================================================================


    def __eq__(self, mat):
        return (mat.rows == self.rows)


# =============================================================================


    def __add__(self, mat):
        """Add a matrix to this matrix and return the new matrix"""

        if self.getRank() != mat.getRank():
            raise MatrixError("Trying to add matrixes of varying rank")

        ret = Matrix(self.m, self.n)
        for i in range(self.m):
            row = [sum(item) for item in zip(self.rows[i], mat[i])]
            ret[i] = row

        return ret


# =============================================================================


    def __sub__(self, mat):
        """ Subtract a matrix to this matrix and return the new matrix"""

        if self.getRank() != mat.getRank():
            raise MatrixError("Trying to add matrixes of varying rank")

        ret = Matrix(self.m, self.n)
        for i in range(self.m):
            row = [item[0] - item[1] for item in zip(self.rows[i], mat[i])]
            ret[i] = row

        return ret


# =============================================================================


    def __mul__(self, mat):
        """ Multiple a matrix to this matrix and return the new matrix"""
        matm, matn = mat.getRank()
        if self.n != matm:
            raise MatrixError("Trying to add matrixes of varying rank")

        mat_t = mat.getTranspose()
        mul_mat = Matrix(self.m, matn)

        for x in range(self.m):
            for y in range(mat_t.m):
                mul_mat[x][y] = sum([item[0]*item[1] for item in zip (self.rows[x], mat_t[y])])

        return mul_mat


# =============================================================================


    @classmethod
    def _makeMatrix(cls, rows):
        m = len(rows)
        n = len(rows[0])

        if any([len(row) != n for row in rows[1:]]):
            raise MatrixError("inconsistent row length")
        mat = Matrix(m, n, init=False)
        mat.rows = rows

        return mat


# =============================================================================


    @classmethod
    def makeRandom(cls, m, n, low = 0, high = 10):
        """ Make a random matrix with elements in range(low-high)"""

        mat = Matrix(m, n, init=False)
        for _ in range(m):
            mat.rows.append([random.randrange(low, high) for _n in range(n)])
        
        return mat


# =============================================================================


    @classmethod 
    def makeZero(cls, m, n):
        rows = [[0]*n for _ in range(m)]
        return cls.fromList(rows)


# =============================================================================


    @classmethod
    def makeId(cls, m):
        rows = [[0]*m for _ in range(m)]
        idx = 0

        for row in rows:
            row[idx] = 1
            idx += 1 

        return cls.fromList(rows)   


# =============================================================================


    @classmethod
    def fromList(cls, listOfLists):
        """ 
        Create a matrix by directly passing a list
        of lists
        """

        rows = listOfLists[:]
        return cls._makeMatrix(rows)