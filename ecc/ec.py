"""
Defines an elliptic curve group
"""
# from tonelli import prime_mod_sqrt
import os.path
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
import algebra

inf = "Infinity"

# a number mod p
class pnum(algebra.Element):
    def __init__(self, n, p=None):
        if type(n) == int or type(n) == long:
            self.value = n % p
            self.prime = p
        elif type(n) == type(self):
            self.value = n.value
            self.prime = n.prime
        else:
            raise TypeError("Can't make pnum from {}", n)
    
    def __str__(self):
        return str(self.value)
    
    def __mul__(self, other):
        if type(other)==type(self):
            return pnum(self.value * other.value, self.prime)
        else:
            return pnum(self.value * other, self.prime)
    
    def __add__(self, other):
        if type(other)==type(self):
            return pnum(self.value + other.value, self.prime)
        else:
            return pnum(self.value + other, self.prime)
    
    def __sub__(self, other):
        if type(other)==type(self):
            return pnum(self.value - other.value, self.prime)
        else:
            return pnum(self.value - other, self.prime)
    
    def __mod__(self, other):
        if type(other)==type(self):
            return pnum(self.value % other.value, self.prime)
        else:
            return pnum(self.value % other, self.prime)
    
    def __rmul__(self, other):
        if type(other)==type(self):
            return pnum(self.value * other.value, self.prime)
        else:
            return pnum(self.value * other, self.prime)
    
    def __radd__(self, other):
        if type(other)==type(self):
            return pnum(self.value + other.value, self.prime)
        else:
            return pnum(self.value + other, self.prime)
    
    def __rsub__(self, other):
        if type(other)==type(self):
            return pnum(other.value - self.value, self.prime)
        else:
            return pnum(other - self.value, self.prime)
    
    def __rmod__(self, other):
        if type(other)==type(self):
            return pnum(other.value % self.value, self.prime)
        else:
            return pnum(other % self.value, self.prime)
    
    def __eq__(self, other):
        if type(other) == type(self):
            return self.value == other.value and self.prime == other.prime
        else:
            return self.value == other
    
    def __hash__(self):
        return str.format("{}p{}", self.value, self.prime).__hash__()
    
    def __div__(self, other):
        if type(other) == type(self):
            return self*other.inv()        
        else:
            return self*(pnum(other, self.prime).inv())
    
    def __repr__(self):
        return self.__str__()
    
    def inv(self):
        return self**(self.prime-2)
    
    def Order(self):
        return p-1
    
    def identity(self):
        return pnum(1, self.prime)
        

# a point in the elliptic curve
class point(algebra.Element):
    """
    the class of a point on the elliptic curve
    """
    
    @classmethod
    def curve(cls, x, A, B, p,):
        """
        This is the equation for the curve, the the cubic side.  The other side is assumed to be a perfect square.
        """
        return (x**3 + A * x + B)%p
        
    def is_valid(self):
        return self.curve(self.x, self.A, self.B, self.prime) == self.y**2
    
    def identity(self):
        """
        returns the "point at infinity"
        """
        return point(inf, inf, self.A, self.B, self.prime)
    
    @property
    def x(self):
        if self != self.identity():
            return self.value[0]
        else:
            raise ZeroDivisionError("infinity has no x component")
    
    @property
    def y(self):    
        if self != self.identity():
            return self.value[1]
        else:
            raise ZeroDivisionError("infinity has no y component")
    
    def __init__(self, x, y = None, A = None, B = None, p = None):
        if y is None:
            self.value = x.value
            self.A = x.A
            self.B = x.B
            self.prime = x.prime
        else:
            if (type(x) == int or type(x) == long) or isinstance(x,pnum):
                self.value = (pnum(x, p),pnum(y, p))
            else:
                self.value = inf
            self.A = A
            self.B = B
            self.prime = p
    
    def __str__(self):
        return str.format("{}",self.value)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return (self.value == other.value)

    def __mul__(self, other):
        """
        The group operation for elliptic curves         
        """
        
        # degenerate cases
        if other == self.identity():
            return point(self)
        
        if self == self.identity():
            return point(other)
        
        # Case 1, self != other
        try:
            if self != other:
                slope = pnum((other.y - self.y)/(other.x - self.x), self.prime)
                new_x = slope**2 - self.x - other.x            
            else:
                slope = (3*self.x**2 + self.A)/(self.y * 2)
                new_x = slope**2 - 2*self.x
            
            new_y = self.y + slope*(new_x - self.x)
            prod = point(new_x, 0 - new_y, self.A, self.B, self.prime)
            
        except ZeroDivisionError:
            prod = self.identity()
        
        return prod
    
    def __div__(self, other):
        return self*other.inv() 
        
    def Order(self):
        return NotImplemented
        
    def __hash__(self): 
        return self.__str__().__hash__()
        
    def inv(self):
        if self == self.identity():
            return self.identity()
        
        else:
            return point(self.x, 0-self.y)
