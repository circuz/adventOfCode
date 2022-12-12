INPUT = "./day12_input"
# 188 too low

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
                    self.start = (i,j)
                    self.landscape[i,j] = 35
                    continue
                if c == "S":
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
        print("Got all distances!")
        distances_to_a = []
        shortest_distance = 9999999
        for tile in self.distance:
            if self.landscape[tile] == 10:
                distances_to_a.append(self.distance[tile])
                if self.distance[tile] < shortest_distance:
                    shortest_distance = self.distance[tile]
                    print(shortest_distance)
        print("===========")
        print(f'Shortest: {min(distances_to_a)}')

           
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
                    if self.landscape[direction] >= (self.landscape[curr] - 1):
                        self.distance[direction] = self.distance[curr] + 1
                        self.check_next.append(direction)
            self.unvisited.remove(curr)
        return


if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        land = Landscape(lines)
        print(land.start)
        paths = land.find_path()
