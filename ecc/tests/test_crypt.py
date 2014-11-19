import unittest
import priv
import ec
import encrypt
import decrypt
import pub
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
from helpers import *

class crypoTests(unittest.TestCase):
    
    def test_point_encryption(self):
        
        m = ec.point(1,2,priv.A, priv.B, priv.prime)
        cipher = encrypt.encrypt(m, priv.base_point, priv.pub_raised_point)
        m2 = decrypt.decrypt(cipher, priv.exponent)
        
        self.assertEqual(m, m2)
    
    
    def test_full_encryption(self):
        
        text1 = "all ignorance taboggens into know"
        
        #import pdb; pdb.set_trace()
        points = encrypt.text_to_points(text1)
        cipher_points = encrypt.encrypt_text(text1)
        text2 = decrypt.decrypt_points(cipher_points)
        
        self.assertEqual(text1, text2)
    
    
    def test_num_to_point_one(self):
        
        p = pub.num_to_point(1)
        self.assertTrue(p.is_valid())
        
    
    def test_num_to_point_many(self):
        """
        test that numbers get mapped to unique points
        """
        card = 1000
        nums = range(card)
        
        points = [pub.num_to_point(num) for num in nums]
        
        self.assertEqual(len(set(points)), card)
    
    
    def test_num_to_point_to_num(self):
        
        for num in range(15*8)[::4]:
            p = pub.num_to_point(2**num)
            self.assertEqual(pub.point_to_num(p), 2**num)
    
    
    def test_text_to_nums_to_text(self):
        
        text = "all ignorance jcaesoijfeioasjfeioasjfeioajf"
        nums = text_to_nums(text)
        text2 = ''.join([num_to_chars(num) for num in nums])
        self.assertEqual(text, text2)
    
    
    def test_text_to_text(self):
    
        text = "all ignorance toboggens "
        
        points = encrypt.text_to_points(text)
        text2 = decrypt.points_to_text(points)
        
        self.assertEqual(text, text2)
        
