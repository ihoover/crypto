import priv
import arith
import pickle
import sys
import struct

def block_to_chars(block):
    """
    take block (bits), and convert to chars 
    """
    
    binary_block = format(block, 'b')
    
    # it might not have a multiple of 8 bits, so zero pad on right
    if len(binary_block)%8 != 0:
        binary_block = '0'*(8-len(binary_block)%8) + binary_block
    
    chars = []
    for i in range(len(binary_block)/8):
        byte = binary_block[8*i:8*(i+1)]
        chars.append(chr(int(byte, 2)))

    return ''.join(chars)

if __name__ == "__main__":
    
    # string to encrypt
    cyphertext = [int(number.strip('L')) for number in sys.argv[1].strip('[]').split(',')]
    
    # decrypt
    plain_blocks = [arith.powm(block,priv.inverse,priv.modulus) for block in cyphertext]
    
    # turn into characters
    plaintext = [block_to_chars(block) for block in plain_blocks]
    print ''.join(plaintext)
