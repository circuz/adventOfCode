# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 19:23:25 2021

@author: August
"""
key = "####.#.#..####.#.####..#..#####.....#####.###..##.##......###.###.#.....####....####..##.##..####..........##.##...#..##..#.#.###..##...#....#...#..###.#.#####..#..#...#.####..####.#..##.#.#.###.##.##.....###..##....#....#.#.###.##.#..#..#..#######.#.##.#...#....#.....#.#..#.#.##.##.######.#..##.#..##..#####..#..###...##.#.###.#.#..###..###.....####....##...#.####.###.#.#.#..#..##.#..#.##.#.#####.####.#.#...##.####.#######...#....#####.##.#......##.######..###.###...##.##..##..#.#..####.##..#..##.#...#..#.."

scan = ["#..##..###.......##.##.#..##..##...#...####..#.###.#..##.#.#.#.#.##.#.##...#######..##..##.#.#..##.#",
"#...##....#..#####..#.#..##........#..#....##.##....#.##.##.....####...##...#..##.#....#......#...##",
".#..#....#....#..##.#.##.#.##.#..#######....#.#...##..#.##.##..##.###..#...#.#.####.#..#..#####.#..#",
"##.#.#.....##...#..##.#..#####..#..#.####.#.##...##..#..######.#.#.#.#...#..##.###.##...#..#.#.#####",
"#.#.##..###...##..###......##.#.#.######.###.#.#..#.##.#.##.##..#...#..#....#.##.##....#.##...#...##",
"##########.....#..#..##.....#..##.#.##..##..#.##.###...#..#..##.#.#.#.###.#..##.##..###.###.#######.",
"...#.#...##..#.#..#..#.#.###..#....#.#.#.###..###..#......#..#.#.#.##...#..#..#.###.####.#..####...#",
"##..#....##.#...##..##.....#.####.##.#.#...#..######..##.#...##.####.###.#.....##...####..#......#..",
"##.#....###..##.##...#.#.#..#...#..###.#...#.#####.#.##..#.#.###...#####.#.###..#.##.###.#..#....#..",
"..#.#.......###....##.##..#.###.#..#...####...#.#.##.........#..#..##...#...#...#.##.#.#..##.#.#..#.",
".###.###.########.#.##..#.....#####..#.....#..##..###....######.##.##..#..#.#####...##..##.....#.#.#",
"....#....##.#####..###...#..##..#.#.#.######...#.#.##.#......##.##......##..##..#.###.#..#####...##.",
"..##...#######..##.##.####.##.#.#.##.#.#####....#.###....###.......##########....#.#.#....##...####.",
"#.#..#.######....###.###.#.#######.#.....#..#.##...##..######....#....#....##.###.##......#..#.#.##.",
".#...#...#....###...#######.##.#.......#..#...#...#####...##.##.....#.#..#....##..#..##...#.#.#..###",
".#.#.#########..#.###.#.#.#.#....##.#####.##.#.#.......#.#.##.##...#..###...##..###..##...#....#.#.#",
".#.##.#..#.#..##....##.....#.#.#.#.####.#.###..##.#...#..###....##.##..#.##..##...#......#####.#..##",
"####.#...##.#..#.#...####...#...#.#.####..#..#...##..#..#...#.#..##.#.#.##..#...###.###.####.#...###",
"...##..#..#...###.....##.####.....#...#..###..#.....################...####.###..##.####......#.##.#",
"..##..###.#....#......#...#.#.###..####..##...#.#..#.###..######..#.###.###.....#.##..##.#..#.#....#",
".......#..#.........#............#.#..##...###.#..####..#.#..###....##....##.#..#.....#....#....#..#",
".#......######....##..#.##.###..#####...##.#.#...##.#..##.#.##...#.##.##..#...#.########.#####.#...#",
".....#.#.........#.###.#....#..########..####...#....##..#...#.#.#.#.#..##...#..#.###...#.########..",
".#.####.##..##...#.#..###..##.#.#.#.#......#.##.#..###...#.#..###.....#..##....#.....#.#.#.#.#..#...",
".#.#####.##..##.###.##.#..###....###.###...#####.#.#.#####.####..#..##.....###.......#.#..##...#####",
"#..#....###....#.#........###....#....#....###.....###...##.#....##....##.....##...#...##......#.###",
".####.####...##.####...#..###.#..##.#..###.#......#####.#.#..#....##.###..#..#.#####.#.##..#...#..##",
"......#.#.#..#...#.#.......#.##..#.###.#####.#.##.######....##.#..###....#.#.#.###..##..#..#..#...##",
"###..#...##.###...#.#.#####....###...###.......##..#..###..#.##..###.####...######..#..#..#.#.......",
"##.#....###.##.#..#.#..#..###...##.....##.###.#..##...##...##.##.#......#.#...##..##...#..#.####.##.",
"#...#..##.#.####...##.#.#.##.####.#####....#.###.#..#..##.#.#.#...#..#.##..#..#.##.##.###..#.....#.#",
".#.##....#.##....#..#.#...#.#..#####.......#..##....###...#.###.....##.###.#..###.##....#..##.##....",
".#....##....##..#....####.###.#..####.##.#.########.#..#.###.#....###.####..#..#...#######....#.#.#.",
"#.#####...##......##.#.#.#..#.####..#..####.....#.###...#.##.#..#.####.#####..#.####...##.##.###....",
"....####..#..#....####.###.###.##.....#.#.#..##.##.##..###...##.......#..#.##.#...##.#....#.##......",
"#####...#####..###.....#...###..#.##..###...#.#..#...##..###..#......#...#...##.#.###.#####.##.#..##",
"##..#.######.#..#.###...##..##.#..#.#..#######..#.####..######.#......##.#...###...##..##...##....##",
"#..###..#..##..#..####.##..#...#.#..######.#.#######...##..##.#......##.#.##..#..######..#.#.#####.#",
".###.##.##.#....#.#####...#.#.#.##...###.#.##..#.#.#..#.##.........###....#..##.....#.####....##..##",
"....#.###.###.#..#......###.#....#.###.#.#..##..##.#....#.#.##.#..#.#..##.#..#....#..####........##.",
"......#.##..###.#....#.#.#..#.####.....##..##.#..##......##..##.##...#.###.##..#.....#..........###.",
"####.#.#.#......###.#.####...##....#....#.#........##..#..######.#.##.####.#.###..##.#...#.##..#..#.",
"##....#.#.###.#.#...##..##....#...#...###.#....#.#....#..####..##....#.######.#.##.##.####.##..##.##",
"..#........#..###.##.#...##...#.###.#.##.#####.###.#.#..####.#.#.##..#....#.#.#.####..#....#...#.###",
"##...#..#.#...##....#..#.#.#......##.####.#...#........##.#.#.###...###...###........###.##.#....#.#",
".##..#.####.#.##..#...##.###.#.#.#.##.####.##...#......#.#...##..........###.#....#..##..##....####.",
"..##..###.##.###...#.###.#..#..#...####..##..#######..#..#..#.########..#..#....##.###..#..#.#.#####",
".....####..###.#.##....##.####.#....#.#.....#..#...#....######..#.####....##.#.#.#....##..####.#.###",
".##.#..###......####.##.#..#.####.#.#....#.###.#..#####....#...##...######.##..####.#..##.##........",
".......#.....####..#...##.###.#.#.#..#.#.....########.#.###.....####......####.#..#.....###.##...###",
"#..###.#....##.#....##.#..#.#.####.#.###..###.#########....#..####......##.##..##..###.##...#.#..#..",
"#..###.##......####.###.###.#.#.####..#...#.######..#####...##.#.##...##..#..#..#.#.##.####....#...#",
"#..#..#..#.#.##...#.#..##..##.#.######.##.##.####...##.#..##....##.#.##.#.###.##.####....###.##.#.#.",
".#.#..##.#.#.###....#..#.#...#..###.#...##...######...####....#..####.#..#.#.##....#..#...#...#....#",
".####.##...#.......#####.#.#..#.#..#...##...#.#..##.###..#....#..#..##.###.#####....###.#..#.##.####",
"##....###.#....#.##.#.#.#..#...##.##.....##.#....#..##...##.######..#.###.#..##..##.#.###....#...#.#",
".#.##.......#....#..#....#..#.#...##...###.#.#.#.######..####..####.###.###.#.##.....#...##.##....#.",
"....#.###.##.#.##..#.....###..#.#......#.#####.##..#.##..#..###..#..#..#..#####..#.##.#....####.#..#",
"##......##.#.#..#.##...##....##..#..##.#....#.#.###.#.#..#.#####..###.#..###..##..#####..#...#.####.",
"#..#...#..#.#..#..#.#..#.###.#.#...#..##..#.###########.####..###.#.#..#.#.####..##..######.#.#....#",
"#....##..#..#####.###..###.#....#######.####.#....######.####..##.#..##.#..##.#.##....#.#####.#.###.",
"..###....##.#.#...##.#..#.###...#..#..#...########.#....##.###.####..#.#.##.######.#...#...##.##.#.#",
".#..#.#....#.#...#.###.#...#.##.####.#.....#...###...##.##..####.#.#..####..##.###.#.#####.###..####",
".#.#.##.#.#.#.#..#..#####...##..#..####.#..#.##.#.##..#..#..##.##.#.#.#######.....##.##.#....###.#.#",
"##.#.#...##...#.#.#.#..##.##..###.#######.####.##.#..#..####.##..#.#.###.#..###.....#..###.#.##...##",
"###.....####..##..##..###.##...#.##.#..##.###..##.#.##..##..#.#...##.#.#..##....#..##..#....#...####",
"...#.####.#...#.#.###.#.#...##....#..##.##.##.##.#...##......###...#...####..##....###.#..#..##.###.",
".#.#..#.#.#..####.##..##..#..#####.#...#.#.#..#.#.....##.#.....#.......##.....#....###.##.#.#..#....",
"...######..#.#.####.#.#...##...#....#....##.#...###......##..#..#.##....#..###....###...##..#.#.#..#",
"###.####.###..#....##.###.##.#####..#.##..###.###.##.#.##.#####...#..###.#.#..##....#...#.#....###..",
".#.#.#..#.############.#######.#####.##.##....####..##....####.##..#...##.###.......##.........###.#",
"##.#.#..##..#.##..#.#..##.#.###...#####.###.####...#..##..#.##.###...#...##.#..#.#..###.##...#...###",
"##.#...#.#..#.#.#.###....#.#.#.##.##.##.#.....#......###..#.#...###..##...#.##..#...###.....###..#..",
".#..#.#.##..##.##.#.###.##.#.....#.#....##.#...#####....###...#.##...#..#....##.#..####..#...#.#.#.#",
"#.###...#...##.##.#.#.#.####.##.##.######...#..####..#.....####....#.#####....##.###.....#..#.#.#.#.",
"#.#.#.#....###..#.#.....#..#..##..###..#.#.#.....###..####..#.##.##.##.####....###.##.#....###..####",
"###.#.##.#.#.#.#..#..#.##########...####..#.#.##..##...#...#..#..#...#.#..###..#####..###.#....#####",
"##..####...##.....####.###..#.#######.#.##..#.#####.#....#.#....####.#.##...##....##..#.#.###.#.####",
"#.#.#.#.##.#.##.###.....##.#######.##.##..#####..####.#.##########.#.##.#.#....#.#.##..#..##.......#",
"....#.####.###...#..#####.####...#..#..##...#.....#.###...###.######.....#.#..#...#.....####..#.##..",
".##.###.#....#..###.#..#.##.##.#......#.#.#.#.#.##...#.#..####.#.##.###..###...#.#.##....#..#..##...",
"##...####.##.#####.#....##...##...#.##..##.#.......####..#..#.#..#.#..##.#.##.#.###..#.#..###...#.##",
"...#####...###.#.##.#.#.#..#.#.#......#.#.####.#.#...#.....###....###.#.##.###.#.###.#.##.#.#.##.#.#",
"##.#.##.#.#.#####....###.#...##.###..##.###....#####..#.###.##.##.##.##...#.#.#.###.#..##.#...#.....",
"...####.#..#..#..#.#...###..##..###.#.###.##.##.####.#.#.#......#####...##.#..#.##.##.#.....#....##.",
"..#.#..###.#....##....#.#.#..#####.##.##.####..##..#....####..##..####.##.#######......#.#.#..#.##..",
"#.###.#.#.##.#.##..##.#..#.#######..#...#..##..##..##..##....##..####.##..#.#..#.....##.##.####..#.#",
"..##..#..##..##.##.###.##..#####...#..###..####...##..#.....###..#.#.##....##....##.#.##..#.....#..#",
"...#.##..###..#.#.#####..#...#.#.#..#..###.#.#.#.#........#..##..###......#..#.##.#..#.#...###.#.##.",
"#.##...#.#.#...##.......#...#..##...#.#..##...##.#....###.###.#.###...#........###.#####.#.##....##.",
"#.##..#......####..#....###..#.#..########.......#.####...#......######..#...#####.#.#.......#####.#",
"##.##..##.##.###.##.#.....#..##.#.#...###.......##.#.#...........#..#..##.#.##.#.###.#.###.##..#...#",
"...#.#####.##.#.....##..##.##.#..#.#....#.#####.######....####..#..##..#.#.#......##...#.#....##.#..",
"#.#####.#.###..##.#.##...#.#.###.#####.....#.##..##.##..#.##...##.##..########..#..#..###..#.#..####",
"..##.##.....#..#####.##..####.##...#...##.##..#..##.#.######.#.#..###...###...###.##..###....###.##.",
"##.##...#.####.#..#..#.#.#..#...##.#.....##.###.##.###.#.#..##.#.#.....#..#.###.###..#.#..#####.#...",
".###......##..##.#..#......###.##...#..#..........##..#...#..######.#.#.....##....##.##.##.#.##..##.",
"#..##.#..##.##..#####......#.#..###..#.#....#.###..###..##.#.##..###..#.#.###..####.###..#.#....###.",
"..#..#####..#.#...##.##.##.#.#.#####...#...####.....##.##..#..#....#..#.....#......####.#....#.####.",
".#.##.##...###...##.#....####..#####.##.#..#...##.#########.#..#..#.#.##.####.##########...#####..#."]

"""
newscan = ["........................................................................................................................",
".######################################################################################################################.",
".######################################################################################################################.",
".######################################################################################################################.",
".######################################################################################################################.",
".######################################################################################################################.",
".######################################################################################################################.",
".######################################################################################################################.",
".######################################################################################################################.",
".##########.##..###..#######.##.##.##..##..###.#####..#####.##.##.##########.####..########..##..##.####.##.##.########.",
".########.##..###.....######..#.##.##....#.#.#####......######.##..#.##.###...##.##...##.##..#.#.####.##.#..#.#########.",
".##########....###.##...##.##.###.####.....#..####..##.#.#..#.#..####.###.#.##....#....###..#....#..#.#.#..#.#.########.",
".########..###...#.##.....########.#.#..#.##....#######..#.##.#..###.#.#####......######...##..###.#.#.##.#.#..########.",
".########.##..####...##.#..##..#.#.#.#.#.###.#.#...####..#####.#..###.#.#..###.#....#..##.##.###....#.##.##....########.",
".##########.....##.#..#...#.##.#..###....#####.#...#.#.#....#..###...#.#.#...#...#..#...##.#.###..###.#...#############.",
".##########.##..#.###.####.###.#..##.#...###.#...######.#...#..#....##....#..###.####...#########.#.#####.#.#..########.",
".########.##.##...##.###.##.###...#.....#.##...###....##..#.#..#...#####.##..######...#.##..#......#..#..#.##..########.",
".########.#...#..######.##.##.##..#..#..#.#######.####.##....#.##..#.#.##.##.#.#####.##...#.###..#..#....#.#.#.########.",
".##########.....#......#.##.#.##..##.##.####...#..##.#.#.##...#..#.......##.####..##..#.#.####.#####....##.#..#########.",
".###########....#..#.##...##.##.##....#.##.#.....#......#..##..##..##.#..#.#..##.###.####.###.#.###.#.#..#.....########.",
".#########..####.#.##.#....####..#..#####........###.###....##.##......#..#.##.#.#..#.#.#.#.#.##..##..#...##.#.########.",
".##############..###..#...#.#####..####.#####..######..#.#..####...###.#.##..#.#..##.#.#.##.###.##..####.##..#.########.",
".############.#####...##.#.##...##.##.#.##..#.####.#...#..##.###..#.#..####.....##.#..##...##..#..#.##..##.##.#########.",
".########.#..#.###.#..##..##.#.....#.#####.###.##..###..#..#.#.#.#.#........######.#.#.###.....#..####....##.#.########.",
".#########...#...#####..#..##.#.#.##..###..##..###.#..........#..###.#.###.#.##..#.#####..##.#.#.###.###.....##########.",
".##########.######...##.##....#..#.###..#.##.#.####.##....#.....##.#.#.#.#..##...#...#.###..#.##.###...####....########.",
".##########.###...##..###...##.#.#..#.####...##.......#..###.###.#.#.#.#.######....#...##.##...##.###..##......########.",
".########..#.#.###...#...#.#.#..##.....####...#...##..#..##.####.##.#.###.####..##.####.#....###.....###...#.#.########.",
".##########..#.#.#.####.#....##.#####.#.#...####.#...##.####..##.#..###.#.##.#.#.##..##.#...#...#.##...###..##.########.",
".##########...#.#.#...##..#.###..##..##.....###.##.#.##.#.#.##.#..###....###.#.#.##.#..#..#..#.###...##.....#..########.",
".#############.#.###.##..#.##.#...#..#.##.###....#.###..###.####.##.#..#..##.#..####.###....#.#..#####.#..#.#..########.",
".#########...###..#.#..#.#####...####.#..###.##.#####........###..###.##..##.##.#....##.#.#.########.#..##....#########.",
".#########...###..##..##.#.#..#.#.#.#..#.#.###.###....#..##..#.#.......#.####.#.####...##..##..####..##..##.##.########.",
".#########.#.####.####.####....##.#.##.####.#......###.#.##.##.###.###..#.#...#.##..#....#.##..#.##.#.#...###..########.",
".###########....####....###..#..#.#...####...####..###.#.##..#.##..#.###....##..#..##......###.......#.#.####.#########.",
".########.#.#..##..###.##########..#..#.#.##.#..###....#.##.#..#.##...##..#.#..###..##.######....#..#..####..#.########.",
".##########..##.#......#.#...###...#.##..###.##.#.#.#....#.#....#..##..###..##.#..#...##.#.###..#.#..#####..##.########.",
".#########.##....##.###.#..###.#..#.#.#.##....###..#.#...#.#.#..##....##.#.##.###...#.#.##.##......###.##..##.#########.",
".########.##..##.#...#.......###.##.#.####..###..#.##.#....##..##.#..##.#.#####........#.#..#..#.##.##....#.#..########.",
".#########.##..#.##.##...######...###....#####.#####.#.#####.##..##.##...#..#.#.#..##.###..###..#.#.###..#.#...########.",
".#########..#.##..####...###..####.....#..#.###...##.#..#.#.#.#.###.#.##.###..#.....#####.#.####.##..#####..#..########.",
".#########.##.##.####.#....##.##....#..##.#....##.##...##.....##.###..##.##.######..##...###.#######.##.#....#.########.",
".#############.##.#.####..##..#.##..#.###.##.###.#####...##.##.##.###..##.#####.##....#...#####......###..##..#########.",
".########.##..####..#.#..##.#.#.##..#.#.####.##...##...####........#....##..#.##.....#.###...#.#.####.##.#.##.#########.",
".########.#####.##...#.#.##..#.#.#.##.#....#..#.#..#######...#.#..##.#..#.###..##.###.###..##....#.#.###...##..########.",
".########.###.#.#.###.....#.###....#...#...##........###...###.#.#.#...##..###.#....##.#..#..#.######..##...#.#########.",
".#########.#..#.#....#.#...#.#.#..#.....##...#..##...###.##.###.#.##.#..##.###..#..##.....####..#..##.##..#.##.########.",
".#########.########.#....#.....#...#..##.#.##..####.##.#.###..#..##..####..########.#....#...#..#..####.###.#..########.",
".##########..##.###.#.#.#......###########.#..###.###.##.#..##..#.....##.#.#######..##.#.####.#.#.#..##.##.##.#########.",
".###########.##..##.####...#...##.##....###.#...##.#..#....#.####...##.#.....##.##.###..##...#..#.##.####..###.########.",
".############....#...#..###..##.##..#.#.##.#...#.......#.#..#...##..#.###.#..#..##..##..#.#.#..##..###..##.##.#########.",
".########.########.##.##..###.#.##...##.##...#.#.#.##.##.#..#.#.##..#.#####....###..#..####.#######..#.#.#####.########.",
".##########.#.########..##..###..#.##.#.#.###.######.##.###...#..#.#...##.#.##...#.###..##.#.#..##.#..####.#..#########.",
".########.###.####.#..####......###....#....#..##..#.#...#.#..###.#.#...#..##.#..#.##..#.###..##..###...#.#..#.########.",
".########..#...######.#..###.###...#.###...#.#.##.##..#####.####.###.#.##.#.#..##.##.##.###.#....#.###...##...#########.",
".#########..##.#.#.##..###..#...#.##.#.#.###.##.#.##.#...####..##.#.##.###.##.##..#.#....##.....##.....######..########.",
".##########..#....##.#.#.#...##.##........##...####.####.#...##.###.#####.#.###.#.##.....##.#..##..####...#...#########.",
".##########.##..#.......##..#.###..######.########..#.#####..##....#.#.##..##...#...##.#.#.#..####.#...##.##..#########.",
".#########..###.##.###.##.#####..#...#..###.###..##.#.###.####..#.###..#.##.##.#....###..#.###.#..##...#.#####.########.",
".###########.#...###.###.##.#####..###..#.#.#.#.#...###..#.#.....#.....#.##.#.....####.#.#..##....#..##....###.########.",
".########.##.##...#.#...####.#..#.##.#######.##.#.#.#.#.#.....#...#.#...##.#...##.#.......#..##...###..#.......########.",
".#########..#...###.##.###..#...###########....#.#..#......#.##..#....#.##.#..###.###.#..##.#.######...#.....#.########.",
".##########..##.####.#.###.##.##..###.###.....#.######.#...#..#..##.#......#.#.##...##.##.#.####.##..##..#.##..########.",
".#########..#.#.#.#...####.#.#.#..##..#......#.##.#....##.##..#.#....#..#....#####...#..##.#####.##.#.#...##.##########.",
".###########.##......#.#...#.#..######.#.#..#.#...##.##...#######.#####..#..##.#######.#.#.#.##.#...#..#...#.#.########.",
".########.##.##.#######....#..##.#...#...###...#.#.#..#..#.####.#.#########.#.#.#.#..##.##..#..##.##..#.##.##.#########.",
".#########.#..#.#####....##.#.#.##....#.##..#.##.#.#...#.###.#.#.##...###...#.#.###.#.#.##..##.##.#..##.###....########.",
".#########....#...#.#.###....##.##.#..#####.#....##..######.#.#.#.##..#.##.###..###.##..##.##.#.##..#.#..##..#.########.",
".########.#..#######.###...###...#.######....##.#######...#.#.....#..##.##.##.###.##.#####..###..###..#..##....########.",
".###########...#..###.#.##..#.####.#.##.#...##..########....#.#...##.#...#..####....##..##.##.#....#####.#####.########.",
".#########.#...#...#..#.#.#.###...##.#.##.##..#.#...##.#####.#..#######.##.###.#.##.###.#.####..##..#..#..##...########.",
".#########..#..#..###..#....##.#...#......###..#..##...#.###...######.###..##......#..###..####....###..####.##########.",
".#########.####..##.####...#.....#...#.#..##.#.#..#..#.##.###...##.##.#.##.....###.###.###..#######..###.##.##.########.",
".##############...#####.####.##..#.#..####...#.###.##..#.#.##......##.##.#####.##.#.#.####.#.##...###.##..##...########.",
".########....##.##....##.....#...#####.####.#.#.#..#.#####.###.##...#.....#.#.#...##.##.#.#.##.....###..###....########.",
".############.#####..#.###..##.##.###.#...#.###.#.#.#.###.###.###.##.#.###.#.##.##..#.###......#.##....################.",
".##############.#.####.#..#...#.#....###..###........#####.#.#..#....##.####.#.###.#.#..#.#.#.....###..#....##.########.",
".#########.....##..##.###..#....#...#....##.#..###.#.....##...#..#.##....#.#...##..#...#.#####.##.#########..#.########.",
".#########..########.##.#.#.#.#.##..#..#####..##....#.#.###.####.#######....#..#.##.###......#.##..#....#####..########.",
".########..#...#...#......##....##.##..#.#..#.#.#..##.#####.###.#...#.#..........#..#..#.#.#####.#.#.###.##....########.",
".########...#..##.##.##.#.#.#....#.#...#...###..##.######..#######.#.#.##.........#####.#..#.####.###.##.#.#..#########.",
".########...#.#.###..####.###..#.#.#.#..#####.####..##...#.#.####.#######.##.#.#.##.########.#...#.#.###.##..##########.",
".#########.###....#..#....#.####..#.#...#...#.##..#.#.######......#.##.#.##.#.###.#.##.#.#.#.##.###...#....#...########.",
".########..##.###...###.##.###..#...##.##.#..#.#.#####....###....#..##.#.#####.####.##..#######..#.##......#.#.########.",
".########.###.#....#.####.##.#.##....##.#..##..#.##.#.#.##...#.#..#####.#..#..##..###.#..#.#.#.#..#.###.#.#....########.",
".#########.#.####..###.#.....#...#.###.#####.####...#....#..#..#####...#.#.#.#.###.###...#.#.##.##....####..#.#########.",
".###########...#..#..#...#.#.##...#.###.#.#.###.###.#.#.#..###......###..##.######....##.#.#.####.#.#.##.##..#.########.",
".#########....##.##..##.#...##.##..#..#.#.....###.#..#.#....#.###..##.#..##..#...##....#..##.##..#..#..####..#.########.",
".#########.#..###.#..#.#.#.##.#.####.####...#.##.###......#..##..#.#.#..##....#####...#..###.####..#####.###.##########.",
".#########.#...###.###.###.#####.##.#..#.#.#..#...#..##....#.#.##.###....########..#.##.#.#.###.#####..####.##.########.",
".###########....#..########.....##.###.#.##.#.#...#...#..#..####.#.#...#..##..#.##.####...##.#..##.#..#.#.##...########.",
".########...####.#...###.#.#.#..##.##.#.#....#....###..#...........##.#.#.....##..#.###..#######.#.##.#..##.###########.",
".########.####.#...#...#.#.###.###.....#......###.#.#..#.###.#.#.....##....##..#...###.#####...#.#..#####.#############.",
".########..#.#.######..##.###...##.#..##...#.########.####.#.....###.##...###..##.###..#.###.......#.....#####.########.",
".##########..###.#..#..#..###.###.##.######.#.#.###.##.#.##..####.#####.###.#.###.#.#..#.#.##.#.###...#...##..#########.",
".############...##..##.#..#..#.##.#...##.#.#..###..###...#####.##.#..#.##.#.#...####.#########.#..#..#.#.#####.########.",
".########...##.##.#.#.##.#####.###.#..#.........#...##.#...####.#......###.#.#..###....##.#..####.####..#...###########.",
".##########...####.###......##.#.#...#.##....#.....#...#.##...#.#.#.#####.##.....#...##..#.####....#.####...###########.",
".##########...#.#....#..##.....########.##.##.#...###.##.#.#.#..##.##.#.#.#.#..#..#.#.#..#####.....##.#.##..##.########.",
".########.#...####..###....###..#.#..##..#.#....#.##..##.#...######.##.##.##.###.####..###..##...#...#.##.#.#..########.",
".#########..#####.#.#.######....###.#...#..####.#.###.###.####.##.#...####.#..####...###..###.##.##.####.##.###########.",
".###########.....#..#######....#..####.#.#...#.##..#.###.#..#...#.#.###..##....#.#.#.#..#.#...#.##.##..#......#########.",
".########..##..##..###..###...#.#...##.##.##.##.###..#.#.#.###...#######.##..#.##......#.....##.#.....#..#.#...########.",
".########.....####.#.###...######..##..##.##..##...#..#.##.###########..##.#.##..#.##....#.......#.#...#.###...########.",
".########.####.....#####...........#.#..#.######...#####..#.##..#####....##..#####....#.#.#.#.######..#.....##.########.",
".########..#.#..#...##.##..#.#..#.....#..##..#....#..#..#..#.#.#..####.##..###..#..#######..#####.#.##.##..##.#########.",
".########..#.##.#..#...###.#.#######.########...##.###.#####.######...###..##.#.#.#.##.######.#..##..###...#.##########.",
".########.#############.##.#####.##..###..#........#########..##..#..##..####.##.#.#..##....#...#...#...#.#.#.#########.",
".#########...####.#.##..###.#..###.##..##......###...#..#.#..##..#####..#..###.....###...###........#######.#.#########.",
".#########.##..###.#..##.....##.##...##..#.......#..#...#.##...#..#..#.##...##..###...#.........##.....#...############.",
".#################.###.#.######.####..#.##...######.##.######.......###.##.#########..###........#.###...#.##.#########.",
".######################################################################################################################.",
".######################################################################################################################.",
".######################################################################################################################.",
".######################################################################################################################.",
".######################################################################################################################.",
".######################################################################################################################.",
".######################################################################################################################.",
".######################################################################################################################.",
"........................................................................................................................",]
scan = newscan
"""

"""
key = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"

scan = ["...............",
".....#..#......",
".....#.........",
".....##..#.....",
".......#.......",
".......###.....",
"..............."]
"""

def check(x,y,matrix,key):
    binum = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if matrix[y+i][x+j] == "#":
                binum += 2**(1-j) * 8**(1-i)
    #print(binum)
    return(key[binum])
    
def zeros(y,x,n):
    if n%2 == 1:
        c = "."
    else:
        c = "#"
    matrix = []
    for i in range(y):
        row = []
        for j in range(x):
            row.append(c)
        matrix.append(row)
    return(matrix)

def createnewscan(scan,n):
    m = 4
    if n%2 == 0:
        c = "."
    else:
        c = "#"
    newscan = [c*(len(scan[0])+2*m)]
    for __ in range(m-1):
        newscan.append(c*len(newscan[0]))
    for row in scan:
        newscan.append(c*m + row + c*m)
    for __ in range(m):
        newscan.append(c*len(newscan[0]))
    return(newscan)




asd = [0]*50
oldscan = scan
for n in range(50):
    scan = createnewscan(oldscan,n)
    newpixel = zeros(len(scan),len(scan[0]),n)
    for y in range(1,len(scan)-1):
        for x in range(1,len(scan[0])-1):
            newpixel[y][x] = check(x,y,scan,key) 
    
    oldscan = []
    for row in newpixel:
        oldscan.append("".join(row))
        
    asd[n] = oldscan
    print(n)
         
    
for row in asd[49]:
    print(row)
    
# 256:365
# 256:365
#test
# 105:215
        
""
total = 0
for ii in range(len(asd[49])):
    for jj in range(len(asd[49][0])):
        if asd[49][ii][jj] == "#":
            total += 1
            
print(total)
""
