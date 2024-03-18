#!/usr/bin/python3
# Author: MikiasHailu
"""alx interveiw minimum oper"""

def primeFactorization(x):
	""" This function will return  prime factorization of x"""
	div = 2
	array = list()
	while (div <= x):
		if x % div == 0:
		array.append(div)
		x /= div
		else:
		div += 1

		return array


		def minOperations(n):
			""" This function will caluclate the smallest number"""
				min = 0
				factors = [x for x in primeFactorization(n)]
				occurences = {item: factors.count(item) for item in factors}
				for k, v in occurences.items():
					min += k * v
					return min
