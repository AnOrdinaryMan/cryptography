def RSA_encode(m,e,n):
    return pow(m,e,n)

def RSA_decode(c,d,n):
    return pow(c,d,n)

def Inverse_egcd(e,phi_n):
    r0,r1,s0,s1 = 1,0,0,1
    while phi_n != 0:
        q,e,phi_n = e // phi_n,phi_n,e % phi_n
        r0,r1 = r1,r0 - q * r1
        s0,s1 = s1,s0 - q * s1
    return r0 

p = 17
q = 11
N = p * q
phi_N = (p - 1) * (q - 1)
e = 7
# egcd 
d = Inverse_egcd(e,phi_N)


# Sample
M = 88
C = RSA_encode(M,e,N)
print(C)
print(RSA_decode(C,d,N))