"""
Calculator
==========

Build support functions for Linear Algebra operations
"""


# =============================================================================


__author__ = 'Tran Nam Phuong'
__email__ = 'trannamphuong2k@gmail.com'
__date__ = '2021/12/02'
__status__ = 'development'


# =============================================================================


import math


class Vector(object):
    """ Create a vector """
    def __init__(self, *args):
        if len(args) == 0:
            self.values = (0, 0)
        else:
            self.values = args
    
    def norm(self):
        """Returns the norm of the vector

        Args:
            vector (List[float]) : input float number list

        Returns:
            (float) : length of the vector
        """
        return math.sqrt(sum(x*x for x in self))


# =============================================================================


    def inner(self, vector):
        """ Returns the dot product of self and another vector
        Args:
            vector1 (List[float]) : input float number list
            vector2 (List[float]) : input float number list

        Returns:
            (float) : dot product value of 2 vectors
        """
        if not isinstance(vector, Vector):
            raise ValueError('The dot product requires another vector')
        return sum(a*b for a, b in zip(self, vector))
        


# =============================================================================


    def __mul__(self, other):
        """Calculate the dot product of self and other if multiplied
            by another Vector

        Args:
            vector (List[float]) : input float number list
            orther (float|int|vector) : input float number or int number or vector 

        Returns the dot product of self and other if multiplied
            by another Vector
        """

        if isinstance(other, Vector):
            return self.inner(other)    
        elif isinstance(other, (int, float)):
            product = tuple(a * other for a in self)
            return self.__class__(*product)
        else:
            raise ValueError("Multiplication with type {} not supported".format(type(other)))


# =============================================================================


    def __rmul__(self, other):
        """ Called if 5 * self of instance """
        return self.__mul__(other)


# =============================================================================


    def __truediv__(self, other):
        """Calculate division of self and other if multiplied
            by another Vector

        Args:
            vector (List[float]) : input float number list
            orther (float|int|Vector) : input float number or int number or Vector

        Returns:
            division value of self and other if division
            by another Vector
        """
        if isinstance(other, Vector):
            #divided = tuple(self[i] / orther[i] for i in len(self))
            try:
                (other[i] for i in range(len(self)))
                divided = tuple(a / b for a, b in zip(self, other))
            except:
                return 0
        elif isinstance(other, (int, float)):
            try:
                other != 0
                divided = tuple(a / other for a in self)
            except:
                return 0
        else: 
            raise ValueError("Division with type {} not supported".format(type(other)))

        return self.__class__(*divided)


# =============================================================================


    def __add__(self, other):
        """Calculate the vector addition of self and other

        Args:
            vector (List[float]) : input float number list
            orther (float|int|Vector) : input float number or int number or Vector

        Returns:
            the vector addition value of self and other
        """

        if isinstance(other, Vector):
            added = tuple(self[i] + other[i] for i in range(len(self)))
        elif isinstance(other, (int, float)):
            added = tuple(a + other for a in self)
        else: 
            raise ValueError("Addition with type {} not supported".format(type(other)))

        return self.__class__(*added)

        
# =============================================================================


    def __radd__(self, other):
        """ Called if 5 + self for instance """
        return self.__add__(other)

        
# =============================================================================


    def __sub__(self, other):
        """Calculate the vector difference of self and other

        Args:
            vector (List[float]) : input float number list
            orther (float|int|Vector) : input float number or int number or Vector

        Returns:
            the vector difference value of self and other
        """
        if isinstance(other, Vector):
            subbed = tuple(a - b for a, b in zip(self, other))
        elif isinstance(other, (int, float)):
            subbed = tuple(a - other for a in self)
        else: 
            raise ValueError("Addition with type {} not supported".format(type(other)))       
        
        return self.__class__(*subbed)

    
# =============================================================================


    def __rsub__(self, other):
        """ Called if 5 - self for instance """
        return self.__sub__(other)
        
    
# =============================================================================



    def dist(self, other):
        """Calculate distance value for 2 vector

        Args:
            vector (List[float]) : input float number list
            orther (List[float]) : input float number list

        Returns:
            distance value for 2 vector
        """
        if isinstance(other, Vector):
            return math.sqrt(sum((b - a)**2 for a, b in zip(self, other)))
        else:
            raise ValueError("Magnitude with type {} not supported".format(type(other)))
        
    
# =============================================================================


    def __iter__(self):
        return self.values.__iter__()
                
    
# =============================================================================


    def __len__(self):
        return len(self.values)
                
    
# =============================================================================

    
    def __getitem__(self, key):
        return self.values[key]

                
# =============================================================================

        
    def __repr__(self):
        return str(self.values)


# =============================================================================

        
    def __eq__(self, other):
        if(self[i] == other[i] for i in range(len(self))):
            return True
        else:
            return False