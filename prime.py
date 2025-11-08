#!/usr/bin/env python3

def prime(number):
    prime_num = []
    candidate = 2
    count = 0
    while count < number:
        is_prime = True
        for n in range(2, candidate):
            if candidate % n == 0:
                is_prime = False
                break
        if is_prime:
            prime_num.append(candidate)
            count += 1
        if count == number:
            print(prime_num[-1])
        candidate += 1
prime(10001)
