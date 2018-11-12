p = 17
q = 11
N = p * q
phi_N = (p - 1) * (q - 1)
e = 7
# egcd 
d = 23 

M = 88

def RSA_encode(m,n,e):
    return pow(m,e,n)

def RSA_decode(c,n,d):
    return pow(c,d,n)


# Sample
C = RSA_encode(M,N,e)
print(C)
print(RSA_decode(C,N,d))