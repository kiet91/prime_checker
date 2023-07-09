from prime_check import *


def unit_check(n: int):
    f = fact(n).divisors()
    if not prime_checkp(n):
        for i in range(2, len(f)):
            if f[i] + f[i - 1] % f[i - 2] == 0:
                print(f'{n} is not the targeted integer')
                break
            if i == len(f) - 1:
                print(f'{n} is the targeted integer')
    else:
        print(f'{n} is the targeted integer')

unit_check(169) # nhap so nguyen duong bat ky
