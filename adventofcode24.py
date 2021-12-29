# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 10:42:52 2021

@author: August
"""

code = """inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 2
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -5
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -16
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -8
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 2
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -8
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x 0
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -4
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
""".splitlines()

def inp(a,b):
    a = input("PLEASE ENTER A NUMBER: ")
    return(int(a))

def add(a,b):
    return(a+b)

def mul(a,b):
    return(a*b)

def div(a,b):
    if b != 0:
        return(int(a/b))
    else:
        print("ERROR ERROR! DIVIDE BY 0")
        return(a)

def mod(a,b):
    if a<0 or b<=0:
        print("ERROR ERROR! INVALID INPUTS TO MOD FUNCTION!")
        return(a)
    else:
        return(a%b)

def eql(a,b):
    return(int(a==b))



num = 99999745870000

x,y,w,z = 1,1,1,1
i = 0

g = globals()
while z:
    if not num%10000:
        print(num)
    x,y,w,z = 1,1,1,1
    i = 0
    if "0" not in str(num):
        for row in code:
            #com = (row).split(" ")
            #print(com)
            #a = globals()[com[1]]
            a = g[row[4]]
            com = row[0:3]
            if com == "inp":
                g[row[4]] = int(str(num)[i])
                i += 1
            else:
                try:
                    b = g[row[6:]]
                except KeyError:
                    b = int(row[6:])
                if com == "add":
                    g[row[4]] += b
                elif com == "mul":
                    g[row[4]] *= b
                elif com == "div":
                    g[row[4]] = int(a/b)
                elif com == "mod":
                    g[row[4]] = a%b
                elif com == "eql":
                    g[row[4]] = int(a==b)     
    num -= 1
print(num)