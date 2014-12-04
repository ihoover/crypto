import priv
import arith
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
import helpers

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

def decrypt_nums(nums):
    return [arith.powm(block,priv.inverse,priv.modulus) for block in nums]

def decrypt(text):
    
    # turn into array of longs
    cypher_nums = [long(number) for number in sys.argv[1].strip('[]').split(',')]
    
    # decrypt the nums
    plain_nums = decrypt_nums(cypher_nums)
    
    # turn plain_nums into text_to_nums
    plaintext = [helpers.num_to_chars(num) for num in plain_nums]
    
    return plaintext
    
if __name__ == "__main__":
    
    cyphertext = sys.argv[1]
    plaintext = decrypt(cyphertext)
    print ''.join(plaintext)
