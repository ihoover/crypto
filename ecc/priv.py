from ec import *
# from tonelli import prime_mod_sqrt

prime = 2**127 - 1

# 14*A**3 + 27*b**2 != 0
A = -5
B = 8
x,y= 1,2
# for n in range(100):
    # x = n
    # y2 = point.curve(x,A,B,prime)
    # print y2
    # if prime_mod_sqrt(y2, prime):
        # print prime_mod_sqrt(y2, prime)
        # y = prime_mod_sqrt(y2, prime)[0]

        # print x,y


base_point = point(x, y, A, B, prime)    
assert base_point.is_valid()

exponent = 83475621985748721978442157
pub_raised_point = base_point**exponent

