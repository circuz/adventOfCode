import math

INPUT = "./day09_input"
# 347 too low

H = 0

def roundup(x):
    if x > 0:
        return math.ceil(x)
    return math.floor(x)

class Rope():
    def __init__(self):
        #self.start = [0,0]
        self.body = [ [0,0] for _ in range(10) ]
        self.tail_visited = {(0,0)}
        self.movement = { "R": [1,0], "U": [0,1], "L": [-1,0], "D": [0,-1] }
    
    def move(self, direction, steps):
        for _ in range(steps):
            self.body[H][0] += self.movement[direction][0]
            self.body[H][1] += self.movement[direction][1]
            going = self.movement[direction]
            self.update_tail(1)
            #print(f'{self.head} O~~ {self.tail}')
            #print("============")

    def update_tail(self, index):
        if (self.body[index][0] - self.body[index-1][0])**2 + (self.body[index][1] - self.body[index-1][1])**2 > 2:
            self.body[index][0] += roundup((-self.body[index][0] + self.body[index-1][0])/2)

            self.body[index][1] += roundup((-self.body[index][1] + self.body[index-1][1])/2)
            #print("uuuuuuuuuuuuuuu.")
            #print(self.body)
            if index != 9:
                self.update_tail(index + 1)
        self.tail_visited.add(tuple(self.body[9]))

        
def parse(lines):
    rope = Rope()
    for line in lines:
        #print(line)
        rope.move(line[0], int(line[1:-1]))
        #print(rope.body)
        #print("==============")
    return rope.tail_visited
        
     
if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        visited = parse(lines)
        print("\n")
        print(visited)
        print(len(visited))
        
