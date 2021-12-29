# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 14:53:37 2021

@author: August
"""

p1 = 4
p2 = 8
p1 = 10
p2 = 1

score1 = 0
score2 = 0

die = 2
winner = [0,0]

def game(p1,p2,score1,score2,winner):
    dicethrows = [3,4,4,4,5,5,5,5,5,5,6,6,6,6,6,6,6,7,7,7,7,7,7,8,8,8,9]
    
    for dice1 in dicethrows:
        for dice2 in dicethrows:
            p1new = (p1 + dice1)%10
            
            if p1new == 0:
                score1new = score1 + 10
            else:
                score1new = score1 + p1new
                
            
            if (score1new < 21):
                p2new = (p2 + dice2)%10
                if p2new == 0:
                    score2new = score2 + 10
                else:
                    score2new = score2 + p2new
            
                
            if score1new >= 21:
                winner[0] += 1
            elif score2new >= 21:
                winner[1] += 1
                return(0)
            else:
                game(p1new,p2new,score1new,score2new,winner)
    if winner[0]%1000 == 0:
        print(winner[0])
        


game(4,8,0,0,winner)
print(len(winner),sum(winner))
