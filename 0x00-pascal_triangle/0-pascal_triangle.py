#!/usr/bin/python3
""" Author: Mikias Hailu """


def pascal_triangle(n):
	""" pascal triangle """
		if n <= 0:
		return []

		pascal_t = []

		for m in range(n):
	pascal_t.append([])
	pascal_t[m].append(1)

	for k in range(1, m):
		x = pascal_t[m-1][k-1]
	y = pascal_t[m-1][k]
	 pascal_t[m].append(x+y)

	 if(n != 0 and m != 0):
		 pascal_t[m].append(1)

		 return pascal_t
