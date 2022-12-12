INPUT = "./day12_mini"

class Landscape():
    def __init__(self,lines):
        self.landscape = []
        for line in lines:
            self.landscape.append([])
            for c in line[:-1]:
                if c == "E":
                    self.end = (len(self.landscape) - 1,len(self.landscape[-1]))
                    self.landscape[-1].append(36)
                    continue
                if c == "S":
                    self.start = (len(self.landscape) - 1,len(self.landscape[-1]))
                    self.landscape[-1].append(0)
                    continue
                self.landscape[-1].append(int(c,36))
        return 

    def find_path(self):
        self.check_next = [self.start]
        self.unvisited = [ [1] * len(self.landscape[0]) for _ in self.landscape ]
        self.distance = [ [0] * len(self.landscape[0]) for _ in self.landscape ]
        self.height = len(self.landscape)
        self.width = len(self.landscape[0])

        while self.check_next != []:
            self.visit_next_neighbors()
           
    def visit_next_neighbors(self):
        curr = self.check_next[0]
        self.check_next = self.check_next[1:]
        print(curr)
        if self.unvisited[curr[0]][curr[1]]:
            # for asd in [curr - (0,1), (1,0) (0,-1) ...
            # if unvisited.get(asd,0)
            # if mindre än ett steg upp
            # gå dit och sätt distance till förra plus ett
            self.unvisited[curr[0]][curr[1]] = 0
        return


if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        land = Landscape(lines)
        print(land.landscape, land.start, land.end)
        paths = land.find_path()
