from ec import *
from priv import A, B, prime, pub_raised_point, base_point

block_seperator = ' ~ '
pad_length = 8
def num_to_point(num):
    """
    convert number to a point on the curve
    """
    if not(isinstance(num, pnum)):
        num = pnum(num, prime)
    
    # pad it wihth eight bits
    num_shifted = num << pad_length
    
    for k in range(1 << pad_length):
        x = num_shifted + k
        y2 = point.curve(x, A, B, prime)
        try:
            y = y2.sqrt()
            break
            
        except ValueError:
            pass
    
    return point(x,y, A, B, prime)

def point_to_num(p):
    return (p.x >> pad_length).value

