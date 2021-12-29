# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 14:05:04 2021

@author: August
"""
import numpy as np

initial = """.v.>.v>.>.>....>..v>v.>v>v..vv.>...>...v>.v.>.v.v>..v>.v>.>....vv...>.>>>>...>.>>>..>>v>v>.>v>.>>>>..>....vvv..v>.>...>>>v...v...>.>...v.>>
vv....>vv...v>v>.>v..>v>..>.v.>v.v>.>v..>vv..>...v.....>..>.v>.>>v.>v>.....>..>...v.v..vvv>.>..>..v.......>.v>vvvv..>.>v...>..>...v.>....v.
..vvv....>>>.v...>>.....v>..>.v....vv>v>..>..v.v...vvv.>>>v>v..v>>>v..v.>vv.>..v..v.>v..v...v.v.v...>..vv.>.>>.vv...>.v.v.>.vv.>.vv>v>....v
..v..>.>>.v>....vv>.>....>.v>>.>v.>v>...>>.>....v>>.>...v.>>..v.v>v>>...v..v.>..>>.>.>.>>>.....>>>vv.>v.>...v...>>.v.>.....>.>v.v...>.>.v..
....vvv.>...>..v..>..v.....>v>vv>........vvvv.....>.v.v>.v..>..v....v.vvv.v.v>..>.v..>....vv.v....>v..v.>>vv...>..v...>>.v>.>.>.v.>v>.>v..v
....vv....v>.v.v.>...v.>.....>>.>.v.v.v.vv...>.vv>..>>..v>>vv>..>v.>v>>>.vvv.v.vvvv>>....>vv..v......v.......v......>v>..v>.v...vvv.>v>>vv.
...vv..vv>.>..vv.....>vv..>.>v..>v.v>>..>>.>v>...>>v..>>.>....v...v>>..>..v>>>>>.>...>vvv.>>.v.v>.v>..>....v..>v.v>vv>vv>..>.v.v...vvv...v.
v>..vv...v.>>>.>.v>>..>.v....>..>v.>.vv..v....>.>v.>..>..v.v..v>v>...v..v.>v.>>...v>..>..v.v..>..>....v...v...v....>>.>..>.v>>..v>>>.v.....
vv>>vv.>..>v....v>..vv>>v...>v.>>v.>..>>>.v.>vv>v........>....>.v....v...>..>>.>.>>...vvv>.v.v>.>..>.vv>.v.v>...>vv>..vv...>vv.>..>...>v..>
>v.vvv.v>..>>v..vv>.......>.v.v....v..v...v.>>vv..vvv.>....>.>v.>.vv>>>>..>v>>..>.>vvv.v...v...>>v>v>vv..v..>....>>v>v...>v.vvv.>>..v.>>>>v
.>>...v..vv.v.v.>v..v.>...v>.>v>>v.>v......>>>v.>..v>..v>.>...>>vv....v....>vv.vv..v>>v..>.vv.....vv.>>.>.>v...>.>v>.v>..v.v>.v>>.v........
..>v.....v.v.v.v.>vvvv.>v.>>..>..v..>>v.vv>..v.v.>v>v..vvv>vv>.>>>>vv>..>.v..v.v..>..>...v....vv.vv>>vv.>.v>.v.>.>v.v..vv..>...>v.>...>.v>.
vvv...>.>.>..v....>>..v>>.>>>>v.>.vvv...v...>>>>.>v>.>..>..>.vv>.>v>....v..vv.....>.....v>.v.vv>.v...v>v...>....vv>...>.>>v...>v>>>>v.>>.v.
>.v........>....>.vv..>v.vv>....v.>>.v>v.v...v>v.>.vv...>.>vv>....>>vv..v.v.>....v..v>...>...v.>>>vvv....v.v..>.>...>.>v.v>v>v>>..v>.vv.v..
.vv..>>.v>..>.>v..vv>..v>.>vv...v..>>...v>..>v...>.v.>v.v.....>v.>.>>...vv..>.>v....>.>...>.v.v>....v.v.>>>.vvv...>.....v.vv>v..>v>...v>>..
......v.v..vv..vv>..>....>...v........v.>v.v>...>...>>..v.>.>..>..v....>..>v.v.>.>vvvv......>..>vv...vv>.>>...>.v..v.>..>>.v>.>.>.>vv>>....
.>.>vv>.>v>.>vv.v>.vv>>>.v>v.>>v>.>..>>v>>>.v.....>...>...v>v.>..v.v>v>vv.>.>>v..>..v.>>vv..>.>>....v>>>v.v..........v>.>vvv...>.v.>......>
>vv.>.vv>..v..>.v..>vvvv.>.>vv.>v.vvvvv>v.......v..>...>>..>>.v.vvvv.v>.>.....v>v>..v.>..v.......>>....>.v>.v..>.vv.v>v>>.vvv>..v..vv.>v.>.
v>..>>>.>..>>...>...>v>..>v.>..>..v...v>>.v>v>>.v.v>.vvv>.v.>>.>vv>...v...>>>.....>.>>.>v...vv..v..v....>>.......v.>v.v>.>vv.v>.v.>v.vv....
vv...v.>>v..>v>.>>v>v..>..>v...>v.>v.>.vv.vv>>.v.v....vvv.v.vv..v.>>v>>>.v>>>.>>.vv>.>>v.v.>....>.>....>..v>vvv.>....>.vv>v>.v>>....vvvv...
.>.>.>>v.v..vv.>vvvv...>.v.vvv.v...>......v>.......>.....>...v..>vv>>v..>>vvvv.vvvv....>>....vv.......>v>...v.v>>v..>...v.>>>>>..v.v.>.v>..
>>v>...v.v>v...>>...>vvv.>.>>.v..>v..>..>>v>>.>......>.v.v>v.>..>>.v.>>.>.v.>..>.....>....v.vv..v.>v.v.....v>>..>vv...v.vv.v>>>v>.....>...>
>>.v>>>.>.vv>v..v>v.v.v.v>v>>v..........vv......v..vv.....v..v..>>.>..>.v>.vvv..v.v>..v>v.........vv>>v>..>v.....>v...v.>vv>...>..>..>..vv.
>>.v....>>>.vvv>..v.vv..>vvv.>...>v..vv...v...vv..vv....v.>v..>>v...>>>>>>...>>>>v>>>.>..v...vv.>v..v....>....v.vvv...>..>....vvvv>v.v>>v>>
v>.>....v>vv....v..>..>vv>>v>>.vvvv.v.v.>.v.>vv.>v>.v..>vv.....vv.>vv..>.>.....>.vv>>>..v>.vv.>...>>..vv.>v>v>.v>v.vvvvvv..>.>..>.....v..v.
vvv..v>v>>....vv>v...>>v...v.>>>..v>..>v.>.>.>vvv.v...v.>v..v>>>v>..>v..v>>....>>..>v>.v...vvvvvv.>.....v...>.v.v..>vv.v..>>>..v.>>..vvv>>.
.>.v>..v>.v>>...>>>..>>...>..>vv..>..>v..>.vvv>...>..v.vv...>v....>..v.>.v>>v>.>v..vv.....vv...........>.>v>>.v>v.v.vv.v.v.vv.......>>.>.v>
>v.>...>.v.v>v.v.v..>..v.>v.v>.>>>vv.>.>>>>>.v...v>>v.>vv..>.vv..v.v>.>.v.>vv......>...>.>......>..>.>>>.>v.>>v>..>>.v.v....>>>>.....vvv>vv
....>..>....>...>...>..v>....vvvvv>vv>>>.....>....vv>.>v>v.>.v..v.v>.v..>.v>.>.>..v.>v...vv.>>.>>.v.v..v>v>>.vv.>>v..vv>..v.v.v.vv...>.>>..
.>..v.v>v>v>..>>>.v.>>....>.v.v..v..v>.vvv.>.v>..v.>.v..>..>v.v..v.v>vv......v..>v>.>..>v>.v.v.>.>..v>vvv..v..v.v.>.>.v.>.v..v>>..vv>...v..
.>.vvv>>v>.v>.>>.vv.v.>.v.>>..>v>....v..v>..v>.v.....>>v.v.....>..v.>..>.v..>..v..v>...>...v>>>.>vv..>v.>>...>..vv.v.>.>>>.v..>..v>vvv..>..
>....v>>.>>>vvv..v..>.v..vvv>v.>v.>v.....>..v.>.v..v..v..>.>>v>.>v...v>..>.>.>v>.v.v.v.v>vvvv>.>v..v..>>....>>...v......v..v>>>v.v.vv>>>.v>
>..>.v>.v>>...>v.>..v...>..>>>>v.v.>.vv...v.v.v..>..v..>>>.>v>>v.v>v>..>.v.v.v.v.>..>..>>.v...v>>.v...v..>vvv..v...vv.......>.v..>v.vv>..>.
>..v.>>vv>>>v...>.v..v.v..v......>v..v.v.>..vv>...vvv..v.v.>.....vv>vvvv.v..v.>.>>>.>..v>....v>>.......>.v..>.>v.v>...>.v>..vvv>>..vv.v.>.>
>.>>>>.v........>>vv.>..v.vvv>.v>vv>.....v....>v.>>v>..vv..>>...>>>>vv.vvv.vv..>>>......>..>>..>.>......>>>v.....v......v..>.v>>>..>v>v..>.
..>v>..>>..vv>>.v....>...>v...vvv..v.>.v.>...>v..v.v>>.>.>.v.>>.v.>>vv.>>...v..v>.>.....v.>>v....v..>>v.....v...v.>........vvv.....v>v.>.v.
............vv...vvv..>.>>.....v>.vv>.vv...vv...>..vv.v>..v.>...>>.v...vv...........v.>v.>>v..>>>>.>.vv..vvv.>>v>>v>vv.v.v.>..>.v..v.v>.v..
...v>...>>..>>.v.v.v.v..v.v..v>v..>...>..>..........>.v>.v.v...v..vv.>.v...vv>vv>.v.vv.v..>>.v..>.vvvv.>vv......v.vv..v>.>vv>..>>v..v>>>>..
...v.>.>......v>>v>..v...v.vv.vv.v...>...>..vv..v...v.>>...vvv.vv...........v...>.....>vv......>..vv.v>>..>.v>v>>.>>..vv>>vvvv.>>..>.vv>.v.
..v.v>>vv.>.>..>...>......>..>v..>.>....v...>...>v>.v..vv.vv>v.>v....vvv.>.>v>....vvv.v.v.vv.v>.vv.v>.>..v..>..>>.>..v>>>>vv.>v.>..vv.v.v.v
.>v.v.v>v.v.>.>.>>.v>>....>.vv.v..>>>...v>>>>..vvv.vv..v.vvv.v..>.>.>....>v.>>v>.v.>..>..v>vv...>v>..>v.v...v.v....>>.vv>.vv..>.>v.....v>>v
>.....v...>v>v.>>>>>v.v>>v...v.v>>.vv>>v.....v..>>.>.v...>...>>>.v.>>.v>vv.>>..>>>.v>.>.>>>.>...>..>.v....v.>>v>.>>>v...>vv.>v>...vv..v>.v.
>v.>>v>>>>v>v.>vvv.>.v..>vvv>>>>v..vvv>v.>..>...v..>>.v..v..v>...v>...>v>...>v...>..>v>.v.>>..v.>..v>v..v>.v.....>v.>>.>>.>.>v..>..>..>v>..
v>.>>>..vv.v.v..vv.>.....>v.>..vv.vv.v.>.v..v.>>>.v..>v>>v.......vv..v..>.>.....>.>.v.v......vv>.v...v>>.>v.v>>.v..>>.v.vv.vvv>.>>.vv>>>>..
..>...v>>v....v.>..v.>.>>>.>..vvv...>.v.v>>.>.v...v.v.>...v.>v..>>>>...>>>v...v>v....v.v.v..v>.>.>>>.>vv.>.....v>.vv...>.>>>..>..v>.>..vv..
v>..vv........vv>.>.>>..>.v......v.>....vvvvv....>.vvv>v>v...v.v..v.vv>>vv>>>.>>>.v.v.>v.>>..>>v..>...>.v...>.>v.>>..v>>>.v>v>v.>>>...vv...
v>.>..v>>v>..v....>v..>..v.>...vv>.....vv.v>.vv.>...v..v>vvv>.>v.>.>.v.v.v.v.....v.>>.v..>v>>..>>...>>v.>>v>>v..vv>>...>v>>>v>v..v.>..>...>
v>.v.v>>.v.v.>>v..v>.>..>>..>v...v>..v..>.>>>v..vv.>v.>v..vv.v.>.....v...v..>>.>.....>.v>v.vvv>.v.v...v.>..>.>.>v....>v.>>v.v>>...v.>v.v.>.
v.>.v.>...>vv.v.>....>>..vv..v>>v.>v>v>>>vvv.>vv.vvv..v.>v...>.>>v.>.vv>>...>......vv>.....>.>...v>.>...v>..>.>>.v>..v..vvv.>>..v.>.vvv.vv>
....>....vv...v>..>vv.v...>v>v>.vv.....>.vv>.>.v>v.>...v>v>v..vv>>v>v...v.....>...>.....>v.....>>.v.v.>.....v.>v>.>>..>v.>>...v>.....>.v>.>
>...vvv..v>>.>.v.vvv>.>...>vv>.>..vv>>>>...v.>>.>.>.v.v>.vvv....vv.....vv>v..>..>.vv.vv...>v.v....>v>>...v.v.........v.>v>...>..>>.>>vv.v..
..>....v.>...v>v.>..v.>>>>>.>.....v>.>v.v>>.>v>.>.>vv..v..>>>.>>>vvv>>>>.>>.>vvv.vvv..>.v..>..>>>>v>...>..>v>...>>v>v>vv>..>.....v.v.....>>
>...v>..>.vv.v.>.>vvv.>.>vv>vv.>..v.vv>..v>....>.......v..>v>.>v>>.>.>.>.>>v>....v.v>>.>v..v>vv.>>.v.>....v.>>.....>v>v......>>..>.>...>>vv
v....v.>..>v>.v.v>>>vv>>v..vv>>>>>v.vv...v>>.>v..v..vv..v.vvv.>..>vv.v>.v>.vv.vvv.>>>.v>v.v...>..v>v...vv...>.....>v>>>v..v>..>>v.>...v..>.
v......>..vv..v...v>.>>...v.>vv.>..v..v.>vvv.>>v>>.v>.vv>...v>v>.v>v>.v>...v.>>>>..>v>...v>v.v>.>>.>>...v.v...>...v>.v.>>.v..>>>.v>.>v..>v>
......v>>..vv>>.vvv.v>.>>vv.>.v>...>.>>vv>.v..v..>>..>.>.>.>v>..>v.....v..>>.v>.v.vv.v...vv.v..>...v>.>......>..v>>>...>.>vv>>>.v>v.>.>>>v.
..v.>..vvv>v..v...........>>>v...>v>.v..vvvvvv>>v.v..>...v.v>...v>>.>.>.vv>v.v.>...>>>.v.>.v.v>>.>..>>.....v...v.>.....v>.>v>.....>v....>.v
v...>v...>...v.>..>.>>.>.>>>v>..>.vv....>.>>>....>....>..v>..>>>..vv.>v...>..v>..>>..v>>>.>>.v...>..>..>>vv>>>>>v....v..>..>v.>>vv>v.>.>.>.
.>vvv>..>.>v>.v.v..v.....v.v.>>..v.>.>v..v>v.>.>vvv.vv.......v..vv.v...>..>.>v>.>vv...vv...>...v..>>>.vv...>.>....>...>v..v.>.vv>>>..>.v..v
>.v.v.v..vvv>v.v>.>..v.>>vvv.>>>..>.v>v>.............v..>>.>>>vv......v>>v..>......v......v.>>vv...>v>>v.>>>v.v.>>>v...v>.v.>v>..v.v>.>>.>v
>>v.>.v.>.v>.v>vv>>v..v>..v>.>.vv..v..v.>v.>v..vv..v>v.>>.......>v>>>vv>vvv>..v.v..>v>....vv..>...v.v.vvvv..vv.....>>v>.v>>v.>.v..>v.v>>.>.
>.>.......>>>>>>.>.v..v>vv......v.>>....>.>...v.....>.v>..>.v..>>>.>>v....v>.v.vv.v>..v.vv.>..vv.v.>.vv....>>>.>vvv..>.>.>.v>..v.>>.>v...v>
>.v>..v....v.>>..>>....>.v..v..>>v>v>.v..v..v>.>v.>..v.>>.v..v.>>>..v>..>>...v>>...>>v>....>v..>v.v..>>.>vv>>>.vvv...>.v>..>>.v...vvv>.v.v>
v....v.vv>.>....>..>..v.....>v.....vv>..v.>>v.>..>.>.>.>v..>v..>>v.v.>>v.v..vv.>vv...>vvv...>>.>>.vv.>>.>v...vv.v.v.vvv.v>>..v.>vv...vv...>
>>v....v..v..vv.>...v...>>..>.>vv>..>vvv.vv>..v.....>>vv.>...>v>.v...>v.>v.>v>..v.v.>..vvv....v>v..>>.v>..>vv...v....v.v>vv....vv.v..v....v
>vvv>.>.>.vv.>.>vv>v.>>v>..>...>...v>>>>v.v.v>v>.vv>>>v.v...>>.>v.>..>v.vv.vv..>.v..vv>v...vv>v.>.>...>vv>vvv...v.>....v..v.v>v.v.>>vvv...v
...>....v.>.vv>.>vv.>v>..>v...v>.....>v>>.v..>v.....>>..>...>v>>..v.vvv....>v>v..v...>.v...>..vv.>>..>....vv.>v>..>...>..>>>.>>.>v..>..>v..
>.vv.>>vv..v.vv.v>>>.v.v..>.>..vvv...>>>>>.>>>vv>.v.v>.vv.>>....>>.vv.>..>....>.v.....v.v>>..>.>.>...vv.>....>vvv>>.>>v..>..vvv..v>>v>vv>>.
>...vv..v...vv>.>v..>>>>v.vvv.v>..>v>>>>..v>..>v...vv.vv..>>..>..>.....>>v>.....>>v...>.vv...>..v...>>...>>>...>v....vv>.vv>>.....v>v>.>>>>
>v>v>>.>.v..v>vvv.v>vv..>.v.....>v...>.v>>...v>vv>.v.>....>.......>...>.>.>>>.v...v.v>v>.v>vv>>..>>..>..v.v..>..v>vv.v>..>.....vv..v.....>.
>>.....>>>v....>>v.v.v..vv.v..>..>vv.v..v>>.>.>v.v.vv...>>.v>.vv.>>....>...v.>....v>>..>...v...v>>vv....>.....v.v>.....v>>>vv..>...v>.....>
>.vv>.>v.>..v......>.>.vv>.v...v.>>v.>...v>>.v...>..vv>v.v.>>...>v>.>.>....v.v>....>v......>.v....v>.vv...v>v>.>>v.>.v>....v.>...v.......v>
..v..v..>...vv.vv.....>v..>>>...v.vvv..v.>v...v>v>v.>>..>....v..v...v>>.>.>.v.>..>>.v>>>..vv>v..v..>>v..>v.>....v.>..v.>v...v..>>>v..v..>.>
..v...v..>..>...v>...>...>>.>>>v>vv..v>.>>.v.>>v...v....v>.>.>....v...>.>.vv.vv...v.v....>.>.>.>.....vv>>.>.v...>.v.>.v.v..v>.....vv.>..v>v
>v.>>>.>...>..v>>.>vv...>..>.v>.....>.v.vv>>.>>..v>.>.vv>...>...>v.>v>v..>>.>.vv>>vv..>>...>vv>...v...>...v>>>....>.v>vv.v..vv.>v..>..>.>.v
v...>.v>..>..>>.>..vv..>>vv....v>v....v.v...>vv........vvv>v>....>...v..>v...vv.....v..>>.v.>>>.v.vv>....v.>>vv.......>..>.v.v.>..v.v>v.v.>
...>vvv.>v.>>>.vv>v>>.>>.>vv...vvvv...v...v...>.....v...v..v>v..vv..v>...v.>v.>>v...>>>...vv..v.v.v.v>.>v..>v>...v.>v..v.>.vvv>.v...>vv...v
.>.v>>.v..>.v.v...>>>..>v.v..vv..v>......>.>....v.>vv>....>.vv..v>.>v.>v.>..v..>..>.>...v.vvv>>.v>..v....v>...>vv..>>vv..>.>v>.v....>v..v.>
.v>....v.vv..v..v.>v>>.>>....v..v.>v..>v.v>v.v...v>....vvvv..>.v.v.>>v..>v....>.v.vv>v>>>.v..>v..>v.>.......v.>>......>.vv....>>v...vv>v.vv
v.>....v.vvv...>>..v.v>>....>..>>vvv...v...v.>v.vvv.v.v.v...>>>>.>v>...v.vv....v...v.>.v.>>v.vv.v>.>.vv>..v.>.>>....v.>v>.v.v>vv>.>..>>v..>
.v>.v>.>..>v.vv.>v..>vvv>>..>>>v.v>....>v>.>>v..>.....v.v.>>...>>>v>>.....>...>>..>.v...v.v...>....v>v.v....>..>.v.>...>....>>.>.>>........
........v>..v.>.>.>>...>...vv>.>v..>v...>.>v..v.vv...v>.v.v>.v.vv..v..v>v.>v..>>..>..v>.vvvv...v>v.vvv>>>...>..vv.v.>.v>.>.>>....>..>>>...>
..v>v...v>.......>v.>v>.v.v>....v...v>v>v>.>..>>..>.v...v>>vv>.v>>...vvv.>..>>>.>.>>vvv.vv..>v>>v>.>vvv>>.v.>>..v.>.v.>..v.v....>.>..>>..>.
v..v>v>v>....>..vv>v..v>vv....>..>>....>>..v..>>.....>>>.v>.>>v>.v.>..v..vv..v>v>>.v>..v>.v...vv.>vv>.vv.>v.>..>.>.>...>>vvv>>.v...vv>..v..
v..v>.v>.v>v....v>.>.....>.v.>v....>>>v>>>.>...v>.>.v>v..vv..>vv>..vv.>......vv>.>v..vvv.>..>.>.v>...v.vvv.>v>..vv>vv..>v.v>.v...v>..>....v
.>...v...vv.>v>vv.v..>.v>..v.v.v..>...>.....v.....v...>.v..v...>v.>v>v.>>.v>...>..>.>.....v...>>.>v.>.v>>..v..v.>v>.>.>v>.....>....vv>.v..v
vvv.>...v>>>...vv..>>.v.vv>>>v>.>.>vv.v.>.vv.v>..>>>......>vv>v>vv...v...>..v..>>>.>>.>..>>vvvv.v.>v>>vv..v..>v....v>.>>..>v>>vv>.vv.v>>.>.
>.vv>..>.vvv.v>...>.>.>>..v..v..v.>..>>v.vvv>......>..>.>...vv....v>.>vv.>vv.>>v.>>.>vvv..>v.>....vvv>v>>.v>...>.v..v..>..>>>..vv>v.vv>..>>
v...v..>.v.>vvv>.>.v>...v.>>.v.>....>>v.v.v...v>vv.v.>v.>v.>.v>..>.>.v...v..>v>v..v.v..v..>v...v>>.>.>>vv.>.>.>vv>.vv..>.v...vv..vv>.v.vv..
vvv.v>>.v.>...v>.>>..>..v>..>vvvv..>.>.>.v>>vv>>.v..>>.v>>.v..v..>v>.>.vv.>.>....>v...v...>vv>...v>.>...>>>....v.v>.v>v...>v.vv.....v.>>v..
...>...>........vv>.>v>>>v..>....>.vv>vv.>.vvvv>>....v.v.>........vv.v.>...vv.v....>.>..v......vv.>.....>v..>..v.>>v>.>>.v>..v>>.vv>.vv>v>v
....>>.vv...>..v...v..>..>......>...vv...v....>.>..v.>vv>>........v>>.v>vv..v...v...v>..v>...>.vv....v....v>.v>......vv..v......>vv.v>...v.
v....v.>>.....v>..v>>.v>..>>...>>..vv..>..>v.vv>....>..>...>>>vv..v>>v>.>...>.vv.v.v..v.v.v...v>..>>v..v..v>vv>v..>.>vvv.>v>.vv>.vv.>vv>v>v
..v..>v...>.v.>.vvv........>.>..v>...>v.v.v.v>>>.>.vv.v>>>..>.vvv.>>v.vv....>.v.v.v>v>v..vvv...>v.>v>>v>>>>.vv........>v>v.v.v>vv.v.>..>>v.
>vv...>.vvv.v.....v......v.>v.....>>v...v..v..>vv..v..v.....v.vvvvv....>>.v....vvv>......v.vv>.>.>...>v.v>....>>..>vv.>.>>.vv..v>v>..>>.v>>
v>...v.vv>v..v>.v..v.v>.>..v...>...vv>.v.v...>>>...>..>v..>vv.v>v..vv.>v.v..>>.vv......>.>..v..v....>.v.>vvv.v>.v.vvv.vv.>.>....v..>>....>.
v>>vv.>v>.v.>v..>...>v>vv...v>>.>.>v>...>..v>>.....vvvvv..>v>.>v..>...>.v.>>vvv>v.vvv.>>>..>...v..........>vvv>.vv..>v......vv.>v>v..>>v.>v
.....>vv>...vv.v>>>..>.>.v...vv...v.v.v.vv>..v.v....>>.v..vv>>.v.>.>.vvv.v>vv>vv.v.v>....>...>>>>>vvvv.>>vv....>..vv>>v....>v..v>..v>>...>v
..v..v.vvvvv...>v>.v..v..v....>vv...>.>>....>>>.>..>vv>>>v.vv.v.v.v.>.v>.vv..v....>.v..>..v.>>.>vv...>.>v.>..>.vvv>v...vv>v...>.>...>..>..>
v>v.>.vvvv...>.v.>vv.>.>...>.v.....>v...vv...v...>.v.>v.....>v>v.v.........vv.v.vv>..v.>>>.v.>..>v>..v>.vv>>>.v.v...v>.v....v>........v.v>.
v....>>...>>vvv>.>>.>>>.v.v.>.>.>...v>.vv>..>vv..v>v.vv>..v..v...v>>>..vvv.>>v..>>v..v..vv>v....v.>..v....v>>.>>.vvv...v..v.>vv.>>>.>.>>.>.
v>>>.vvv.>.vv.v.....>...v>>.>....>vv.v.v>.>v.vv>>..>v.>.>...vvv.>v.v...>..>v..v...v..v..vv..v.>>.>.>vvv..>.>>>vvv....>>..>>.v.>>>.>v>..v..>
...>.>v.v.vv.vv.>..v>..vv..>..>..>..>v..>>>>v..>....v..v>.>..v...v>>>.>..v>v..v..vv.v>>.v>>.vv..v>...>v>>>.>>>.v...v.>.>vv>v.v>..>v>>..>..>
..>..>..v.>>>...v...>>>.....vv.>..>.v...v>.v..vvvv>...v..vv>.>.vv.>v.v...v.v...>.vv>..>.v...>.v>...>>...v..vvv>>vv.vv......>..vv..vv.vv.>..
.>.>...vv..vv>>.>vv>>v>.>v>.v..v>v>v.vv....>.vvv.>>v>....vv.>.....vv...vvv>>..>v...vv>>...>..v..>.>.>.>....>......v.....>.v..vv>>.....v>..>
.>.>...v>......>>vv.>>.vvvv>>..v.v.v..>.......>>v>>v>.>.vv.v>v...>vvv>.>>>...vv.vvv.v>...>>>vvv...v.>.>>vv.>>v>.>v.>..>.v.vv.v...vv>>..>..>
....>v..v......>vv..v..v.>...>.>>v.>>..v>>..>..vvvv.>..>v.>v.>vv.>.>v.>v>v>v>.>v>..v..v.>v>.>..>...>vv>vv..v....v..>...>v..v.v..>>>>.v.....
>v>.vv.>.>..........>v...vv..vv>.v.v...v..>vvvv.v.>vv.>.....v>..vv.v>>...>.v.v.v..v.>..vv..>.v.v.>..........>..vv.v.v.vv>v.v.v.vv>vv.v.>...
....v>>....v>...v..>v>v..v>>v.vv..>>.>>>>.vv>v..>.v>v.v>....>>v....>vv.vvv..v.>v..v...v...v...v..>v.v.v>.>.>.v...v>.v...>.>.>v..>>.>..>v>v>
>vv.vv.v....>vvvv.v>.v>.v.>...v>.vv....>vv>.>..>>>>..>..>.>v.vv..v.v.>v>..v...v.>.>v.>.v>>v.>..>..>...>.....v.v.>vvv>v>v>v.>..>..>>v..v.v.>
vvv.v.>.>>..vv.>...v>vv>...>....vv.>vv>vv>vv.v...v......>.v.v..v..>>v.>...v.>..v>.vv.>>..>vv...v.v....>>.>>..>..>.>v>..v>v.v.>v>.v..>>..>..
v...v..v.>.>..>v>.....>....>..>v.>>...>v>v...v>>>.v...>>>.......v...>vv>..v>v>.>......v.>>v...v>..>v>.v..vvv>vv..v...vv>.>>.>.>....vv>..v>>
v.v.v.>vv>..>>.>>>..>.v..v>.v>>v>v...>......v..>>..>v....>...vv>.v....>>...>.>..>.....>v>>>vv>...>v>..v.>.vv.v>.v.>v....v.......vv.>.vv.>..
vv>...v>>..>.v>>v>v.vv..>vv>.>.......v.v>>..>>.v>.v..v>.>.v.v>vv>..v..vv....>>v.>>>..v>>v...v>>v...>.vvv......v....>>.>.>....>v..v>>.v.>>.v
.vvv.>vvv...v.vvvvv.>...v....v.v.v.>>>v.>.>v.>.v.vv.vv....v..v>.>...vv>v.>vvv.>v.v.vv>.vv.v>.vv.v.v..>vv>.v>.vvv..v.v....>v.v.vv....>....>>
v.vvvv...>..v>vv.v..>.v>.....>.vvv.>>....vv..v..>v..v.>>..v...v>>.>>.v>.>vv>..v>.>v>>.>.>..>.>..v>...v.....vv.v>v.v..vv>vvvv..>>>>>>.v>v>>.
.>.vv.v...>...>.v>v..>.......v..>....v.>....v>>>>>...>..vvv.>>.>.>>v.>v.v.....vv>...vv.v..>v.>v>....>.v.>.v...>>.v>vv>v.vv.....>>v...v>v...
.vv..v...>.>..v.vv.>>..v>..v...>...v....v>v....v>...>>.v>>>...v.v.vv>>>.>..>>.>..>v...>.>..>..>.>.>vv>>..v.>....v.>.v>.v..vv>..v..v..v....v
v..>>>.>v.>vv.v>>....v.>.v.vvvv>>.>..>.>>.v..>v.v>vv>..>v.v.v.....v>..v...>..>.....>.vv>.v.v..v.v.v....vv.>>>.>vvv>..v>.v>...v..>..>>.>.v>.
>v.>vv.>>..>.>>.>>>.>>.>>v.>.>.v.v>.vv.v.v...>.>.>......>>>v..vv>v..vvv.>.....>.>>>v...>>>v....>v......v...>>>v.>........vv.vv>.>...v>>.v..
>..>>>>.>..>..v>>.v>>..>.>>>>.....>..vv..>.v>..v.v.v.....v...v..vv.v..>vv.vv....vv>vvvv>v>>....v.........v.......v.v.>...v.v>v>v>..v>>v.>..
v......v...v>...>>.>>v>..v>.>.>>.v.v.>.v>.>v....v.>.v.>v>v..v.>..>.>.>>..vvvv....v.>v>>....>..vv..v>>.>v>v>.>vv.vv....>.vv.vv.vv>..>.>....v
....vv>>..v>.>>...v>..>.>...>v>.v>v>>v>>>vvv.>>.>v...>...v.v.v..>..>.v.>..v..>...>..>>>.>>.>vv.vv.>...>.>.v..>.>.>v.>.>>.>v.v>..v.......>.v
vvvvvv>..v>...>v.v..>.v.v....vv..v>.>.v..>vv..>v...>..>>..v>>vv.v.>.v>.......v.>>>>.vv>v>.>.vvv..>v.vv.>.vv.>.v>v>v>v...v....v>v.>..v....>>
.>v.>.>.>...>>.v>>>........>>.>.v.v>.>.v.v.>..>.v>..>.vv.>vvvvv.v..>>>..>>>.>v.v.......>....>vvv..v.>>.vv.>vv>..v..v..>>>..v.>..>>.>>.>.v>.
v>....vvv........v.>vv>.>..v>..v>v..vv....>...>.vv.v>>>..>v...>.v.>v..v..>.>.vv....v.>v.v.vv..>>vvv>>.>..v>>>.v>>>..vv..v>v..>>v>.v.v......
.......vv.vv..>...>..>.>>..>.>>....>>.vv..v...v...>>.v.v.>v..v....>>v.....>..>..v...vv.>......>>>.>v.v.v>v.>..vv...>.vv...v>v>v..v.vv.>>.v>
.>......>v.>..vv.v>v>.v.....>.v.>>v....v>vv.>v>>..vvv..>...v>...v..>..v.>v.>...>..vv>...vv..v....>v..>>vv.v..>v.>.v.v>.v.v>v..v....>..>v...
.v.>...>>>>v>>..>v.v..>v..v......>>>.vv.vv...>.>v...>>.v.v.....v>..v.>.>.v.>...vv..>v.v>>.>>>...>v>.v>>vv.>.v>>v.>>>..v...>...>..>.>>v.vvv>
........>.>v.vvv>....vvv>v.v>.....>>v.>.v..>..>.>.>.>>..>vvv....v.v.vv>>>...v.>...>v.vvv>..>>.>>.vv.vv.>.>..v...>v..v>.......v>>v.vv.>.>..v
.v......>>vv>v.>vv..>..>....>.vvv.>...>.v>>.v...v...>..>vv....>>...v.>..>.v>vv...>v.v..v...>..>>.v>v>v.v.>v.v>..>vv...>..>v..vv.>v>.v>...v.
>....>...>..vv.v>..v..>.>..>....>...v>vv....v.>>.>vv>..>.>v>.....v..>...v..>.>v.>.v.v.>..>.>>>v........>.vvvv...vv..>...>.v>...>..>.vv>...v
v.>>..vv.>v..vv>..>..>.>..v...>v..v>>>..>v>v.v>vv.>.v.>>.v.v.>...>...>>>>>..>v>.v..>.v...>.>..>>.vvvvv...v>v..>.>>.>..v..>>...>.>..vvvvvv..
>>.vv>..>..vvv...v>.>.v..>>.>..vvv.>.>..>.>...>..>>......>...>.>>>..>..vv.v.v...v...>v>v>.....>v..vv.>v..>.v..vv..v.vv..v.>v>.>v>v...v...>v
..>.>...>>.v>v...........v.v.vv>v>>v..>>..>>.v>..vv>vv>..vv>>v.v...>.>...v>.>..v>....v..>...>.v..v..>vvv>...>>.>.>.>.>>v.>>>v..v>v>>>v>>...
.>.v..vvv....>>..vvv.vv..>vv.>.v..>.>.v..v.>>...v....v>.vv.>.>vv...>vv....>vv.....vv.>.>v>>.>vvv..>>.v.v>.>>vv>v.vv.>v.vv..v.vv>...vvv.v.>v
....>....>>v>>v>.>.v>....v.>.v.>..v.v..>.>v..v..v>vv.>v..>..vv.>>.>....v...>.>>>..v..v.v...vv.v.v..v.>..v>>v.>.>vv.v...>>...>v>.v>..>.....v""".splitlines()

def getcave(sizex,sizey):
    a = ["." for x in range(sizex)]
    b = [a for y in range(sizey)]
    return(np.array(b))

def getcuties(cave):
    easties, southies = [], []
    for y, row in enumerate(cave):
        for x, cutie in enumerate(row):
            if cutie == ">":
                easties.append([y,x])
            elif cutie == "v":
                southies.append([y,x])
    return(np.array(easties), np.array(southies))
            

def movecuties(easties,southies,sizex,sizey):
    done = 1
    neweasties = np.array([[-1,-1]])
    for i,cutie in enumerate(easties):
        test = np.add(cutie,[0,1])
        test[1] = test[1]%sizex
        #print(test)
        if not (test == easties).all(1).any() and not (test == southies).all(1).any():
            #print(f"wohoo! East {cutie} moved to {test}!")
            done = 0
            neweasties = np.append(neweasties,[test],axis=0)
        else:
            neweasties = np.append(neweasties,[cutie],axis=0)
            
    newsouthies = np.array([[-1,-1]])
    for i,cutie in enumerate(southies):
        test = np.add(cutie,[1,0])
        test[0] = test[0]%sizey
        if not (test == neweasties).all(1).any() and not (test == southies).all(1).any():
            #print(f"wohoo! South {cutie} moved to {test}!")
            done = 0
            newsouthies = np.append(newsouthies,[test],axis=0)
        else:
            newsouthies = np.append(newsouthies,[cutie],axis=0)
    return(neweasties[1:],newsouthies[1:], done)

def printcuties(easties,southies,sizex,sizey):
    cave = getcave(sizex,sizey)
    for y in range(sizey+1):
        for x in range(sizex+1):
            if ([x,y] == easties).all(1).any():
                cave[x,y] = ">"
            elif ([x,y] == southies).all(1).any():
                cave[x,y] = "v"
    for row in cave:
        print("".join(row))

sizex, sizey = len(initial[0]),len(initial)

easties, southies = getcuties(initial)

#printcuties(easties,southies,sizex,sizey)

done = 0
num = 0
while not done:
    if not num%10:
        print(num)
    #print("==========")
    num += 1
    easties, southies, done = movecuties(easties, southies, sizex, sizey)
    #printcuties(easties,southies,sizex,sizey)
print(num)

