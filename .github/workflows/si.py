from prime_check import *


def unit_check(n: int):
    f = fact(n).divisors()
    if not prime_check(n):
        for i in range(len(f) - 2):
            if f[i + 2] + f[i + 1] % f[i] != 0:
                print(f'{n} is not the targeted integer')
                break
            if i == len(f) - 2:
                print(f'{n} is the targeted integer')
    else:
        print(f'{n} is the targeted integer')


unit_check(7) # nhap so nguyen duong bat ky
