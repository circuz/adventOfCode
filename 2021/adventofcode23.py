# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:25:17 2021

@author: August
"""
import numpy as np

cave = """
#############
#...........#
###.#.#.#.###
  #.#.#.#.#
  #########
"""
#cave is 1,2,3,4, 5,6,7,8,9,10,11
#            12  14  16   18
#            13  15  17   19

tiles = cave.count(".")
cost = np.zeros((tiles,tiles))

for i in range(tiles):
    if i < 11:
        for j in range(tiles):
            if j < 11: #0-index
                cost[i,j] = abs(i-j)
            elif j%2:
                cost[i,j] = cost[i,j-9] + 1
            else:
                cost[i,j] = cost[i,j-1] + 1
    else:
        for j in range(tiles):
            if j <= 10: #0-index
                cost[i,j] = cost[j,i]
            elif j%2:
                cost[i,j] = cost[i,j-9] + 1
            else:
                cost[i,j] = cost[i,j-1] + 1

for row in cost:
    print(row)