import arith
p = 2**521 - 1
q = 2**607 - 1
modulus = p*q
secret_modulus = (p-1)*(q-1)

# now find exponent
exponent = 65537

while arith.gcd(exponent, secret_modulus) != 1:
    exponent += 1

inverse = arith.inverse(exponent, secret_modulus)
