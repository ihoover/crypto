"""
Defines an elliptic curve group
"""
from tonelli import prime_mod_sqrt
import os.path
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
import algebra


# the prime, to which everything is mod
p = 709

def curve(n):
    """
    This is the equation for the curve, the the cubic side.  The other side is assumed to be a perfect square.
    """
    
    A = 3
    B = -3
    return (n**3 + A * n**2 + B)%p 

# a number mod p
class pnum(algebra.Element):
    def __init__(self, n):    
        self.value = n % p
    
    def __str__(self):
        return str(self.value)
    
    def __mul__(self, other):
        if type(other)==type(self):
            return pnum(self.value*other.value)
        else:
            return pnum(self.value*other)
    
    def __eq__(self, other):
        if type(other) == type(self):
            return self.value == other.value
        else:
            return self.value == other
    
    def __hash__(self):
        return self.value.__hash__()
    
    def inv(self):
        return self**(p-1)
    
    def Order(self):
        return p-1
    
    @classmethod
    def identity(cls):
        return pnum(1)
        

# a point in the elliptic curve
class point(algebra.Element):
    def __init__(self, n):
        pass
