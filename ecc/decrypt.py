import priv
import pub
from ec import *
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
from helpers import num_to_chars
from pub import point_to_num


def decrypt(cipher, exponent):
    """
    decrypt a cypher of the form (p1, p2)
    p1, p2 are point objects
    """
    
    ephemeral_key = cipher[0] ** exponent
    m = cipher[1]/ephemeral_key
    
    return m


def points_to_text(points):
    """
    convert plain-points to text
    """
    
    nums = [point_to_num(p) for p in points]
    text_array = [num_to_chars(num) for num in nums]
    
    return ''.join(text_array)


def decrypt_points(points):
    
    plain_points = [decrypt(p, priv.exponent) for p in points]
    return points_to_text(plain_points)

if __name__ == "__main__":
    
    blocks = sys.argv[1].split(pub.block_seperator)
    
    cipher = []
    for block in blocks:
        c1 , c2 = block.strip("()").split("), (")
        c1 = [long(c) for c in c1.split(',')]
        c2 = [long(c) for c in c2.split(',')]
    
        p1 = point(c1[0], c1[1], priv.A, priv.B, priv.prime)
        p2 = point(c2[0], c2[1], priv.A, priv.B, priv.prime)
        
        cipher.append((p1,p2))
    print '\n'
    print decrypt_points(cipher)
