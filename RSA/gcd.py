def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a

# Sample
print(gcd(16,40))