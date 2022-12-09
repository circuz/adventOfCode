INPUT = "./day09_input"
# 6482 too low (6483 too lol)

class Rope():
    def __init__(self):
        #self.start = [0,0]
        self.head = [0,0]
        self.tail = [0,0]
        self.tail_visited = {(0,0)}
        self.movement = { "R": (1,0), "U": (0,1), "L": (-1,0), "D": (0,-1) }
    
    def move(self, direction, steps):
        for _ in range(steps):
            self.head[0] += self.movement[direction][0]
            self.head[1] += self.movement[direction][1]
            self.update_tail(direction)
            print(f'{self.head} O~~ {self.tail}')
            #print("============")

    def update_tail(self, direction):
        if (self.tail[0] - self.head[0])**2 + (self.tail[1] - self.head[1])**2 > 2:
            #print("too far!")
            self.tail[0] = self.head[0] - self.movement[direction][0]
            self.tail[1] = self.head[1] - self.movement[direction][1]
            
         
        self.tail_visited.add(tuple(self.tail))

        
def parse(lines):
    rope = Rope()
    for line in lines:
        rope.move(line[0], int(line[1:-1]))
    return rope.tail_visited
        
     
if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        visited = parse(lines)
        print(len(visited))
        
