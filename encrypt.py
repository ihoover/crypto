import sys
import pub
import arith

if __name__ == "__main__":
    
    # string to encrypt
    plaintext = sys.argv
    
    # turn into numbers
    plain_bytes = [ord(c) for c in plaintext[1]]
    
    # turn gorups of 'length' into unsigned 64 bit values
    plain_nums = []
    working_num = 0
    length = 0
    block_length = 64
    for byte in plain_bytes:
        working_num <<= 8
        working_num += byte
        length+=1
        if length == block_length:
            plain_nums.append(working_num)
            working_num = 0
            length = 0

    if length != 0:
        plain_nums.append(working_num)
    
    print plain_nums
    
    # encrypt
    cyphertext = [arith.powm(byte, pub.exponent, pub.modulus) for byte in plain_nums]
    print cyphertext
