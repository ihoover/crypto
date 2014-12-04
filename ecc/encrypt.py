import sys
from pub import *
import random
import ec
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
import helpers


def encrypt(plain_point, base, raised_base):
    """
    Encrypts a point of an elliptic curve
    """
    
    e = random.choice(range(5,1000))
    random_exponent = pnum(2, prime)**e
    
    cipher1 = base ** random_exponent.value
    cipher2 = plain_point * raised_base ** random_exponent.value
    
    return (cipher1, cipher2)     


def text_to_points(text):
    """
    
    """
    nums = helpers.text_to_nums(text, 15)
    points =  [num_to_point(num) for num in nums]
    return points


def encrypt_text(text):
    
    points = text_to_points(text)
    cipher_points = [encrypt(p, base_point, pub_raised_point) for p in points]
    return cipher_points


if __name__ == "__main__":
    
    # string to encrypt
    plaintext = sys.argv
    print plaintext
    cipher = encrypt_text(plaintext[1])
    
    ret = block_seperator.join([str(ciph) for ciph in cipher])
    print ret
