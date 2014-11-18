"""
Common utilities for text encryption
"""

def text_to_nums(text):
    
    # turn into numbers
    plain_bytes = [ord(c) for c in text]
    
    # put the bytes into blocks
    plain_nums = []
    working_num = 0
    length = 0
    block_length = 15
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
    
    return plain_nums


def num_to_chars(block):
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
