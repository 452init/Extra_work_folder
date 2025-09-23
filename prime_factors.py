#!/usr/bin/ env python3
def prime_factors_generator(n):
	while n % 2 == 0:
		yield 2 
		n = n//2

	for num in range(3, int(n**.5)+1, 2):
		while n % num == 0:
			yield num
			n = n//num
	if n % num != 0 and n > 1:
		yield n

for factor in prime_factors_generator(35):
	print(factor)
