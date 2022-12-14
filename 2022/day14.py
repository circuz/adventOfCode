INPUT = "./day14_input"

def create_cave(min_x, max_x, min_y, max_y):
    min_y += -12
    max_y += 2
    min_x += -1
    max_x += 2
    cave = { (x,y):"." for x in range(min_x,max_x) for y in range(min_y, max_y) }
    return cave

def show_cave(cave):
    dictofdicts = {}
    for coord, value in cave.items():
        if coord[1] not in dictofdicts:
            dictofdicts[coord[1]] = {}
        dictofdicts[coord[1]][coord[0]] = value
    for key0 in sorted(dictofdicts):
        for key1 in sorted(dictofdicts[key0]):
            print(dictofdicts[key0][key1],end="")
        print("")
        
def rockit(cave, rocks):
    i = 0
    while i < len(rocks) - 1:
        xes = sorted([rocks[i+1][0], rocks[i][0]])
        yes = sorted([rocks[i+1][1], rocks[i][1]])

        for x in range(xes[0],xes[1]+1):
            cave[(x,rocks[i][1])] = "#"
        for y in range(yes[0],yes[1]+1):
            cave[(rocks[i][0],y)] = "#"
            
        i += 1
    return cave

def parse(lines):
    min_x = 999
    max_x = -999
    min_y = 999
    max_y = -999
    allrocks = []
    for line in lines:
        rocks = eval("[(" + line.replace(" -> ","),(").replace("\n",")]"))
        allrocks.append(rocks)
        for rock in rocks:
            min_x = min(min_x, rock[0])
            max_x = max(max_x, rock[0])
            min_y = min(min_y, rock[1])
            max_y = max(max_y, rock[1])
    cave = create_cave(min_x, max_x, min_y, max_y)
    for rocks in allrocks:
        cave = rockit(cave, rocks)
    return cave

def next_sand(cave, drop_x, drop_y, max_y):
    x = drop_x
    y = drop_y
    while cave[(x,y+1)] == "." or cave[(x-1,y+1)] == "." or cave[(x+1,y+1)] == ".":
        if y+1 == max_y:
            return False
        if cave[(x,y+1)] == ".":
            y += 1
        elif cave[(x-1,y+1)] == ".":
            y += 1
            x -= 1
        elif cave[(x+1,y+1)] == ".":
            y += 1
            x += 1
    cave[(x,y)] = 'o'
    return True

def start_droppin(cave):
    sands = 0
    drop_x = 500
    drop_y = 0 
    max_y = max(cave)[1] - 1
    print(drop_y)
    while next_sand(cave, drop_x, drop_y, max_y):
        sands += 1
        #show_cave(cave)
    return sands

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        cave = parse(lines)
        show_cave(cave)
        print(min(cave))
        print(max(cave))
        print("")
        sands = start_droppin(cave) 
        show_cave(cave)
        print(sands)
