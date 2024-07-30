#!/usr/bin/python3
"""Author: Mikias Hailu"""


def island_perimeter(grid):
    """This fucntion is called island perimeter funciton"""
    counter = 0
    grid_max = len(grid) - 1
    lst_max = len(grid[0]) - 1

    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                    # for left and right
                if land_idx == 0:
                    # for left side
                    counter += 1

                    # for right side
                    if lst[land_idx + 1] == 0:
                        counter += 1
                elif land_idx == lst_max:
                    # for left side
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # for right side
                    counter += 1
                else:
                    # for left side
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # for right side
                    if lst[land_idx + 1] == 0:
                        counter += 1

                # for top and down
                if lst_idx == 0:
                    # for top side
                    counter += 1

                    # for bottom side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1
                elif lst_idx == grid_max:
                    # for top side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # for bottom side
                    counter += 1
                else:
                    # for top side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # for bottom side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1

    return counter
