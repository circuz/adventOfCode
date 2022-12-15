INPUT = "./day15_input"

def create_cave(lines) -> dict[tuple:str]:
    """ create a dictionary of tuples (coords) and place sensors and beacons """
    cave = {("o","s"):{}}
    extreme_points = {"max_x" : -1, "max_y" : -1, "min_x" : 9999999, "min_y" : 9999999}
    sensors = []
    beacons = []

    for line in lines:
        [sensor, beacon] = line.split(": closest beacon")
        x = int(sensor.split("x=")[1].split(", y")[0])
        y = int(sensor.split("y=")[1])
        cave[(x, y)] = "S"
        sensors.append((x,y))
        update_extreme_points(extreme_points,x,y)
        x = int(beacon.split("x=")[1].split(", y")[0])
        y = int(beacon.split("y=")[1])
        cave[(x, y)] = "B"
        beacons.append((x,y))
        update_extreme_points(extreme_points,x,y)
    """ 
    for i in range(extreme_points["min_x"],extreme_points["max_x"]+1):
        for j in range(extreme_points["min_y"],extreme_points["max_y"]+1):
            if (i,j) not in cave: 
                cave[(i,j)] = "."
    """
    cave[("o","s")] = {"sensors": sensors, "beacons": beacons}
    return cave

def show_cave(cave):
    dictofdicts = {}
    for coord, value in cave.items():
        if coord[1] not in dictofdicts:
            if coord == ("o", "s"):
                continue
            dictofdicts[coord[1]] = {}
        dictofdicts[coord[1]][coord[0]] = value
    for key0 in sorted(dictofdicts):
        for key1 in sorted(dictofdicts[key0]):
            print(dictofdicts[key0][key1],end="")
        print("")
 
def update_extreme_points(extreme_points, x, y) -> dict[str:int]:
    """ update extreme points if some points are outside the extreme """
    extreme_points["max_x"] = max(extreme_points["max_x"], x) 
    extreme_points["min_x"] = min(extreme_points["min_x"], x) 
    extreme_points["max_y"] = max(extreme_points["max_y"], y) 
    extreme_points["min_y"] = min(extreme_points["min_y"], y) 
    return

def get_no_beacons(sen, bea, row=2000000) -> set:
    """ do some clever thinking to see what elements in the row have no beacons """
    checked = set()
    beacons_in_row = set()
    for (s,b) in zip(sen, bea):
        length = abs(s[0] - b[0]) + abs(s[1] - b[1])
        surp = length - abs(row - s[1])
        for x in range(s[0] - surp, s[0] + surp + 1):
            checked.add(x)
        if b[1] == row:
            beacons_in_row.add(b)
    print(len(checked) - len(beacons_in_row))
    return checked

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        cave = create_cave(lines)
        print("asd")
        #show_cave(cave)        
        checked = get_no_beacons(cave[("o","s")]["sensors"],cave[("o","s")]["beacons"])
