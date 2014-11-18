import sys
import pub
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
import arith
import helpers


if __name__ == "__main__":
    
    # string to encrypt
    plaintext = sys.argv
    
    # turn into numbers    
    plain_nums = helpers.text_to_nums(plaintext[1])
    
    # encrypt
    cyphertext = [arith.powm(byte, pub.exponent, pub.modulus) for byte in plain_nums]
    print cyphertext
