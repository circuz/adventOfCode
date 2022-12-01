# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:50:59 2021

@author: August
"""

reboot_steps = """on x=-32..18,y=-49..-2,z=-43..3
on x=-15..35,y=-31..16,z=-9..43
on x=-22..23,y=2..47,z=-35..13
on x=-45..8,y=-18..27,z=-34..17
on x=-15..31,y=-41..9,z=-35..19
on x=-28..21,y=0..46,z=-27..27
on x=3..49,y=-29..15,z=-45..4
on x=-41..8,y=-29..22,z=-48..-2
on x=-22..27,y=-46..-2,z=-12..37
on x=-19..25,y=-5..41,z=-49..0
off x=-37..-28,y=-17..0,z=-12..-1
on x=-14..39,y=-30..23,z=-42..9
off x=0..17,y=-11..8,z=33..47
on x=-14..33,y=-33..21,z=-4..40
off x=-34..-15,y=8..21,z=27..46
on x=-46..8,y=-20..25,z=-19..31
off x=-27..-10,y=7..22,z=-8..9
on x=-10..36,y=-36..9,z=-8..36
off x=6..19,y=-22..-13,z=-1..17
on x=-21..26,y=-20..34,z=-30..18""".splitlines()


def copylolol(lolol):
    copy = [[[] for l in lol] for lol in lolol]
    for i, lol in enumerate(lolol):
        for j, l in enumerate(lol):
            copy[i][j] = [k for k in l]
    print(copy)
    return(copy)

def newlolol(size):
    new = [[[0 for x in range(size)] for l in range(size)] for lol in range(size)]
    return(new)

def turnon(inst,cubes):
    for x in range(inst[0][0],inst[0][1]+1):
        for y in range(inst[1][0],inst[1][1]+1):
            for z in range(inst[2][0],inst[2][1]+1):
                cubes[x][y][z] = 1

def turnoff(inst,cubes):
    for x in range(inst[0][0],inst[0][1]+1):
        for y in range(inst[1][0],inst[1][1]+1):
            for z in range(inst[2][0],inst[2][1]+1):
                cubes[x][y][z] = 0

def sumlolol(cubes):
    total = 0
    for layer in cubes:
        total += sum([sum(l) for l in layer])
    return(total)
    
    
cubes = newlolol(100)

for row in reboot_steps:
    if "on" in row:
        instructions = row[3:].split(",")
        instructions = [x[2:].split("..") for x in instructions]
        instructions = [[min(max(int(x),-50),50)+49 for x in l] for l in instructions]
        
        print(f"on: {instructions}")
        turnon(instructions,cubes)
        
    elif "off" in row:
        
        instructions = row[4:].split(",")
        instructions = [x[2:].split("..") for x in instructions]
        instructions = [[min(max(int(x),-50),50)+49 for x in l] for l in instructions]
        turnoff(instructions,cubes)
        print(f"off: {instructions}")
    else:
        print(f"wtf? {row}")  

print(sumlolol(cubes))