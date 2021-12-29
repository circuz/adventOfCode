# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 12:05:20 2021

@author: August
"""
def flash(y,x,octopi,flashes):
    flashes += 1
    octopi[y][x] = 0
    if y == 0:
        ii = [0,1]
    elif y == len(octopi)-1:
        ii = [-1,0]
    else:
        ii = [-1,0,1]
    if x == 0:
        jj = [0,1]
    elif x == len(octopi[0])-1:
        jj = [-1,0]
    else:
        jj = [-1,0,1]
    for i in ii:
        for j in jj:
            if octopi[y+i][x+j] != 0:
                octopi[y+i][x+j] += 1
                if octopi[y+i][x+j] > 9:
                    octopi,flashes = flash(y+i,x+j,octopi,flashes)
    return(octopi,flashes)

squids = [
"2478668324",
"4283474125",
"1663463374",
"1738271323",
"4285744861",
"3551311515",
"8574335438",
"7843525826",
"1366237577",
"3554687226"]

octopi = [list(squid) for squid in squids]
octopi = [[int(x) for x in row] for row in octopi]

flashes = 0
done = False
steps = 0
while done == False:
    steps += 1
    octopi = [[octopus+1 for octopus in row] for row in octopi]
    for y in range(len(octopi)):
        for x in range(len(octopi[0])):
            if octopi[y][x] > 9:
                oldf = flashes
                octopi,flashes = flash(y,x,octopi,flashes)
                if (flashes-oldf) == 100:
                    done = True
print(steps)
