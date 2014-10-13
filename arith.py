"""
Basic modular arithmetic operations
"""

def powm(base, power, mod):
    """
    Raise the base to the power, mod mod
    """
    
    # convert the power to a binary string
    bin_pow = format(power, 'b')
    
    # loop through the binary digits from least significant to most (so in reverse order of the string)
    prod = 1
    square_power = 1
    for bit in bin_pow[::-1]:        
        # compute next power of two (base ^ (2^n))
        if square_power == 1:
            square_power = base
        else:
            square_power = (square_power ** 2) % mod
        
        if bit == '1':
            prod = prod * square_power % mod
    
    return prod


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

def inverse(num, mod):
    """
    copmute multiplicative inverse mod mod
    """
    
    cd, x, y = egcd(num, mod)
    return x%mod
    
    
