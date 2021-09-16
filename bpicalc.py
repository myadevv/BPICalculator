from math import log
from math import pow

def PGF(x):
    return (1 + (x-0.5) / (1-x))

def BPI(s, k, z, m):
    # s = (Player's score)
    # k = (Kaiden average score)
    # z = (World record score)
    # m = (MAX score of the song)
    
    ss = s/m
    kk = k/m
    zz = z/m

    S = PGF(ss)
    K = PGF(kk)
    Z = PGF(zz)

    SS = S/K
    ZZ = Z/K

    if s >= k:
        return (100 * (pow(log(SS), 1.5) / pow(log(ZZ), 1.5)))
    else:
        return (-100 * (pow(-log(SS), 1.5) / pow(log(ZZ), 1.5)))

print(BPI(3201, 3365, 4156, 4220))
print(BPI(2133, 2220, 2568, 2596))
print(BPI(2336, 2733, 3527, 3648))
print(BPI(1799, 2092, 2787, 2826))
print(BPI(2344, 3504, 4749, 4802))
