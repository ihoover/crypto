import unittest
from ec import *

class TestPnum(unittest.TestCase):
    
    def setUp(self):
        self.prime = 709
        self.A = -5
        self.B = 9
        
        self.p1 = pnum(5, self.prime)
        self.p2 = pnum(4, self.prime)
        
    def test_inv(self):
        
        self.assertEqual(self.p1.inv() * self.p1, 1)
    
    def test_div_pnum(self):
        
        
        self.assertEqual(self.p1/self.p2, self.p1 * self.p2.inv())

    def test_div_int(self):
        
        self.assertEqual(self.p1/4, self.p1 * self.p2.inv())
        
    def test_pnum_init(self):
        
        p3 = pnum(self.p1)
        self.assertEqual(self.p1, p3)
        self.assertIsNot(self.p1, p3)
    
    def test_sub(self):
        
        
        self.assertEqual(self.p1 - self.p2, 1)
    
    def test_rsub(self):
        
        self.assertEqual(5 - self.p2, 1)
    
    def test_rmul(self):
        
        
        self.assertEqual(5 * self.p2, self.p1 * self.p2)
    
    def test_radd(self):
        
        
        self.assertEqual(5 + self.p2, self.p1 + self.p2)

    
    def test_mul_point(self):
        p = point(0,3, -5, 9, 709)
        self.assertEqual(curve(p.x), p.y**2)
        p2 = p*p
        self.assertEqual(curve(p2.x), p2.y**2)
        
        
