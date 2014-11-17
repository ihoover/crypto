import sys
from pub import *
import random
import ec
if __name__ == "__main__":
    
    # string to encrypt
    plaintext = sys.argv
    
    # turn into numbers
    plain_bytes = [ord(c) for c in plaintext[1]]
    
    # convert plaintext arggh!
    
    m = ec.point(1,2, A, B, prime)
    random_exponent = long(3**(3**(1/random.random())))
    
    cipher1 = base_point ** random_exponent
    cipher2 = m * pub_raised_point ** random_exponent
    
    print (cipher1, cipher2)
