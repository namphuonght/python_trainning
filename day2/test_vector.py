"""
Test
==========

Build test functions for Vector class
"""


# =============================================================================


__author__ = 'Tran Nam Phuong'
__email__ = 'trannamphuong2k@gmail.com'
__date__ = '2021/12/09'
__status__ = 'development'


# =============================================================================

import random
import numpy as np

from vector import Vector


# ==========================================================================


def vector_rand(N, length = None):
    """
    Returns a random vector
    """
    if not length:
        return Vector(np.random.randint(N, size =1))
    v = np.random.randint(length, size=N)
    return Vector(*v)


# ==========================================================================


def cal_mul(v, u):
    """
    Calculate dot product of two vectors
    Args:
            v (Vector) : input int number list
            u (Vector) : input int number list

        Returns:
            dot product value of two vectors (int)
    """
    return sum(a * b for a, b in zip(u, v))


# ==========================================================================


def cal_rmul(v, n):
    """
    Calculate product of vector and a number
    Args:
            v (Vector) : input int number list
            n (float) : float number 

        Returns:
            multipiled value of vector and a number (Vector)
    """
    rmul = tuple(a * n for a in v)
    return Vector(*rmul)


# ==========================================================================


def cal_truediv(v, u):
    """
    Calculate division of two vectors
    Args:
            v (Vector) : input int number list
            u (vector) : input int number list 

        Returns:
            division value of two vectors (Vector)
    """
    try :
        (u[i] != 0 for i in range(len(u)))
        div = tuple(a / b for a, b in zip(v, u))
        return Vector(*div)
    except:
        return 0
    


# ==========================================================================


def cal_add(v, u):
    """
    Calculate the vector addition of two vectors
    Args:
            v (Vector) : input int number list
            u (vector) : input int number list 

        Returns:
            addition value of two vectors (Vector)

    """
    add = tuple(a + b for a, b in zip(u, v))
    return Vector(add)

# ==========================================================================


def cal_radd(v, n):
    """
    Calculate addition of vector and a number
    Args:
            v (Vector) : input int number list
            n (float) : float number 

        Returns:
            addition value of vector and a number (Vector)
    """
    radd = tuple(a + n for a in v)
    return Vector(*radd)


# ==========================================================================


def cal_sub(v, u):
    """Calculate the vector difference of two vectors

        Args:
             v (Vector) : input int number list
             u (vector) : input int number list 

        Returns:
            the vector difference value of two vectors (Vector)
    """
    sub = tuple(a - b for a, b in zip(v, u))
    return Vector(*sub)


# ==========================================================================


def cal_rsub(u, n):
    """
    Calculate the vector difference of vector and a number
    Args:
            v (Vector) : input int number list
            n (float) : float number 

        Returns:
            difference value of vector and a number (Vector)
    """
    rsub = tuple(a - n for a in u)
    return Vector(*rsub)


# ==========================================================================


def test_mul():
    N = 5
    length = 10
    v = vector_rand(N)
    u = vector_rand(N)
    assert v * u == cal_mul(v, u)


# ==========================================================================


def test_rmul():
    len_vector = 6
    length = 10
    v = vector_rand(len_vector, length)
    n = random.random()
    assert v * n == cal_rmul(v, n)


# ==========================================================================


def test_truediv():
    len_vector = 7
    length = 3
    v = vector_rand(len_vector, length)
    u = vector_rand(len_vector)
    assert v / u  == cal_truediv(v, u)


# ==========================================================================


def test_add():
    len_vector = 8
    v = vector_rand(len_vector)
    u = vector_rand(len_vector)
    assert v + u == cal_add(v, u)


# ==========================================================================


def test_radd():
    len_vector = 9
    length = 5
    v = vector_rand(len_vector, length)
    n = random.random()
    assert v + n == cal_radd(v, n)


# ==========================================================================


def test_sub():
    len_vector = 5
    v = vector_rand(len_vector)
    u = vector_rand(len_vector)
    assert v - u == cal_add(v, u)


# ==========================================================================


def test_rsub():
    len_vector = 5
    v = vector_rand(len_vector)
    n = random.random()
    assert v - n == cal_radd(v, n)




