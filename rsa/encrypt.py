import sys
import pub
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
import arith
import helpers

def encrypt_nums(nums):
    
    return [arith.powm(byte, pub.exponent, pub.modulus) for byte in nums]

def encrypt_text(text):
    
    nums = helpers.text_to_nums(text, 127)
    return encrypt_nums(nums)

if __name__ == "__main__":
    # string to encrypt
    plaintext = sys.argv[1]
    
    # turn into numbers    
    plain_nums = helpers.text_to_nums(plaintext)
    
    # encrypt
    cypher = [arith.powm(byte, pub.exponent, pub.modulus) for byte in plain_nums]
    print encrypt_text(plaintext)
