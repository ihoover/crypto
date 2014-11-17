from priv import *
from ec import *

if __name__ == "__main__":
    
    c1 , c2 = sys.argv[1].strip("()").split("), (")
    c1 = [long(c) for c in c1.split(',')]
    c2 = [long(c) for c in c2.split(',')]
    
    p1 = point(c1[0], c1[1], A, B, prime)
    p2 = point(c2[0], c2[1], A, B, prime)
    
    ephemeral_key = p1 ** exponent
    m = p2/ephemeral_key
    
    print m
