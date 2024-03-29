INPUT = "./day12_input"
# 482 too high
# 400 too low

def plus(a, b):
    c = list(a)
    for i,n in enumerate(b):
        c[i] += n
    return tuple(c)

class Landscape():
    def __init__(self,lines):
        self.landscape = {} 
        for i,line in enumerate(lines):
            for j,c in enumerate(line[:-1]):
                if c == "E":
                    self.end = (i,j)
                    self.landscape[i,j] = 35
                    continue
                if c == "S":
                    self.start = (i,j)
                    self.landscape[i,j] = 10
                    continue
                self.landscape[i,j] = int(c,36)
        self.height = i
        self.width = j
        return 

    def find_path(self):
        self.check_next = [self.start]
        self.unvisited = [ (y,x) for x in range(self.width+1) for y in range(self.height+1) ]
        #print(self.unvisited)
        #print("=======")
        self.distance = { (y,x) : 9999999999999 for x in range(self.width) for y in range(self.height) }
        self.distance[self.start] = 0
        #print(self.distance)

        while self.check_next != []:
            self.get_check_next()
        #print(self.landscape)
        #print(self.distance)
        print(self.distance[self.end])
        print("===========")
        print(self.unvisited)
           
    def get_check_next(self):
        curr = self.check_next[0]
        self.check_next = self.check_next[1:]
        #print(curr)
        if curr in self.unvisited:
            dirs = [ plus(curr,dydx) for dydx in [(0,1),(-1,0),(0,-1),(1,0)] ]
            for direction in dirs:
                #print(f'Jag har inte gått till {direction} än, det borde jag göra!')
                if direction in self.unvisited:
                    #print("den är inte besökt...")
                    if self.landscape[direction] <= (self.landscape[curr] + 1):
                        self.distance[direction] = self.distance[curr] + 1
                        self.check_next.append(direction)
            self.unvisited.remove(curr)
        return


if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        land = Landscape(lines)
        print(land.start, land.end)
        paths = land.find_path()
