# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 11:16:09 2021

@author: August
"""

def lolcopy(list_of_lists):
    copy = []
    for row in list_of_lists:
        a = [x for x in row]
        copy.append(a)
    return(copy)


def getstrength(path,ind):
    strength = 1
    if (path[ind].lower() == path[ind]):
        strength = 0.5
    if (path[ind] == "start"):
        strength = 0
    return(strength)

def getstrength2(path,ind,special_cave):
    strength = 1
    if (path[ind].lower() == path[ind]):
        strength = 0.5
        if path[ind] == special_cave:
            strength += 0.3
    if (path[ind] == "start"):
        strength = 0
    return(strength)


def getpaths(con,row,caves,num):
    #print(caves[row])
    xcon = lolcopy(con)
    if row == (len(con)-1):
        #print("Wohoo!")
        return(num + 1)
    for i in range(len(con[0])):
        if (con[row][i] >= 0.5):
            """
            for asd in xcon:
                if asd == xcon[row]:
                    print(">" + str(asd))
                else:
                    print(asd)  
            """
            xxcon = lolcopy(xcon)
            if con[row][i] < 0.9:
                for x in range(len(con)):
                    xxcon[x][i] -= 0.25
            num = getpaths(xxcon,i,caves,num)
    #print("Dead end!")
    return(num)



""
paths = [
    ["vn","DD"],
    ["qm","DD"],
    ["MV","xy"],
    ["end","xy"],
    ["KG","end"],
    ["end","kw"],
    ["qm","xy"],
    ["start","vn"],
    ["MV","vn"],
    ["vn","ko"],
    ["lj","KG"],
    ["DD","xy"],
    ["lj","kh"],
    ["lj","MV"],
    ["ko","MV"],
    ["kw","qm"],
    ["qm","MV"],
    ["lj","kw"],
    ["VH","lj"],
    ["ko","qm"],
    ["ko","start"],
    ["MV","start"],
    ["DD","ko"]]

caves = ["start","end"]
for path in paths:
    for cave in path:
        if cave not in caves:
            caves.append(cave)
#lägg "end" sist
caves.pop(1)
caves.append("end")

con = [0]*(len(caves))
connections = [[0]*len(caves) for __ in con]



for path in paths:
    mat = [0,0]
    for i in [0,1]:
        mat[i] = caves.index(path[i])
    connections[mat[0]][mat[1]] += getstrength(path,1)
    connections[mat[1]][mat[0]] += getstrength(path,0)

copiedconnections = lolcopy(connections)
number = getpaths(copiedconnections,0,caves,0)
print(number)

small_caves = []
for cave in caves:
    if cave.lower != cave:
        small_caves.append(cave)
small_caves.pop(len(small_caves)-1) # ta bort end
small_caves.pop(0) # ta bort start
total = number
for cave in small_caves:
    con2 = [0]*(len(caves))
    connections2 = [[0]*len(caves) for __ in con2]
    for path in paths:
        mat = [0,0]
        for i in [0,1]:
            mat[i] = caves.index(path[i])
        connections2[mat[0]][mat[1]] += getstrength2(path,1,cave)
        connections2[mat[1]][mat[0]] += getstrength2(path,0,cave)
    number2 = getpaths(connections2,0,caves,0)
    print(number2-number)
    total += number2 - number
print(total)