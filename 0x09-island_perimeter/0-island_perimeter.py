#!/usr/bin/python3
#Author: Mikias Hailu
"""Answer for the task"""


def island_perimeter(grid):
	"""This is island perimeter funciton with grid pararmeter"""
		counter = 0
		grid_max = len(grid) - 1
		lst_max = len(grid[0]) - 1

		for lst_idx, lst in enumerate(grid):
			for land_idx, land in enumerate(lst):
				if land == 1:

				if land_idx == 0:

				counter += 1

				if lst[land_idx + 1] == 0:
				counter += 1
				elif land_idx == lst_max:

				if lst[land_idx - 1] == 0:
				counter += 1

				counter += 1
				else:

				if lst[land_idx - 1] == 0:
				counter += 1

				if lst[land_idx + 1] == 0:
				counter += 1

				if lst_idx == 0:

				counter += 1

				if grid[lst_idx + 1][land_idx] == 0:
				counter += 1
				elif lst_idx == grid_max:

				if grid[lst_idx - 1][land_idx] == 0:
				counter += 1

				counter += 1
				else:

				if grid[lst_idx - 1][land_idx] == 0:
				counter += 1

				if grid[lst_idx + 1][land_idx] == 0:
				counter += 1

				return counter
