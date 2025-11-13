#!/usr/bin/env python3

# solution by sieving out all even number
def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    if number < 0:
        raise ValueError('negative positions cannot be prime')

    count = 0
    last_prime = 0
    candidate = 2

    while count < number:
        if candidate == 2:
            is_prime = True

            count += 1
            last_prime = 2
            candidate = 3

        else:
            is_prime = True

            for num in range(2, int(candidate**.5)+1):
                if candidate % num == 0:
                    is_prime = False
                    break
            if is_prime:
                last_prime = candidate
                count += 1
            candidate += 2
    print(last_prime)
prime(6)

# using helper function to generate prime numbers

def prime(number):

    while count < number:
        if candidate == 2:
            is_prime = True
            count += 1
            last_prime = 2
            candidate = 3
            continue

        if is_prime_number(number_to_check):
            last_number = candidate
            count += 1
        candidate += 2
    return last_prime

def is_prime_number(n):
    is_prime = True
    for num in range(2, int(n**.5)+1):
        if n%num == 0:
            return False
    return True

#using generators

def prime(number):
    *_, nth_prime = itertools.islice(prime_num(), number)
    return nth_prime


def prime_num():
    candidate = 2

    while True:
        is_prime = True
        for num in range(2, int(candidate**.5)+1):
            if candidate % num == 0:
                is_prime = False
                break
        if is_prime:
            yield candidate
        candidate += 1
