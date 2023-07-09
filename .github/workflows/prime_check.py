from math import *


def prime_check(n: int) -> bool:  # kiem tra neu mot so la snt
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True



class fact:  # phan tich so
    factors: list[int]

    def __init__(self, n: int):  # tach so thanh thua so nguyen to
        self.factorsnew = None
        self.factors = []
        self.n = n
        while (n & 1) == 0:
            self.factors.append(2)
            n >>= 1
        for d in range(3, 1 << 60, 2):  # lui 0001 60 lan ve ben trai (binary)
            if d * d > n:
                break
            while n % d == 0:
                self.factors.append(d)
                n //= d
        if n > 1:
            self.factors.append(n)

    def raw(self):  # tra ve gia tri cua __innit__()
        return self.factors

    def divisors(self):  # tra ve tat ca cac uoc nguyen duong cua n
        divs = [1, self.n]
        for i in range(2, isqrt(self.n) + 1):
            if self.n % i == 0: divs.extend([i, int(self.n / i)])  # sang nguyen to
        divs.sort()
        factorsnew = []
        for i in divs:
            if i not in factorsnew:
                factorsnew.append(i)
        return factorsnew


def prime_checkp(n: int) -> bool:
    f = fact(n).divisors()
    q = len(f)
    if f[1] ** (q - 1) == f[q - 1]:
        return True
    else:
        prime_check(n)

#print(fact(49).divisors())
#print(prime_checkp(371293))
