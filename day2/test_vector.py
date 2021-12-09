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


def vector_rand(N, ran_value = None):
    """
    Returns a random vector
    """
    if not ran_value:
        zero_list = tuple()
        for _ in range(N):
            zero_list += (0,)
        return Vector(*zero_list)
    v = tuple()
    for _ in range(N):
        v += (random.randrange(0, ran_value),)
    return Vector(*v)



t1 = vector_rand(5)
t2 = vector_rand(5, 9)
print(t1)
print(t2)
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
    return sum(a * b for a, b in zip(v, u))


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
    add = tuple(a + b for a, b in zip(v, u))
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
    value_rand = 10
    v = vector_rand(N, value_rand)
    u = vector_rand(N, value_rand)
    assert v * u == cal_mul(v, u)


# ==========================================================================


def test_rmul():
    len_vector = 6
    value_rand = 10
    v = vector_rand(len_vector, value_rand)
    n = random.random()
    assert v * n == cal_rmul(v, n)


# ==========================================================================


def test_truediv():
    len_vector = 5
    value_rand = 10
    v = vector_rand(len_vector, value_rand)
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
    value_rand = 5
    v = vector_rand(len_vector, value_rand)
    n = random.random()
    assert v + n == cal_radd(v, n)


# ==========================================================================


def test_sub():
    N = 5
    value_rand = 9
    v = vector_rand(N, value_rand)
    u = vector_rand(N, value_rand)
    assert v - u == cal_add(v, u)


# ==========================================================================


def test_rsub():
    N = 5
    value_rand = 9
    v = vector_rand(N, value_rand)
    n = random.random()
    assert v - n == cal_radd(v, n)




