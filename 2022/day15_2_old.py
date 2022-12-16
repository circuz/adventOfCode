INPUT = "./day15_input"

def create_cave(lines):
    """ create a dictionary of tuples (coords) and place sensors and beacons """
    sensors = []
    beacons = []

    for line in lines:
        [sensor, beacon] = line.split(": closest beacon")
        x = int(sensor.split("x=")[1].split(", y")[0])
        y = int(sensor.split("y=")[1])
        sensors.append((x,y))
        x = int(beacon.split("x=")[1].split(", y")[0])
        y = int(beacon.split("y=")[1])
        beacons.append((x,y))
    return (sensors, beacons)

def get_radii(sensors, beacons):
    length = []
    for (sen, bea) in zip(sensors, beacons):
        length.append(abs(sen[0] - bea[0]) + abs(sen[1] - bea[1]))
    return length

def circles_haha_not_at_all_circles( sensors, radii ):
    circles = {}
    for (sen, rad) in zip(sensors, radii):
        circles[sen] = []
        print(f"new circle! number {len(circles)}")
        #print(sen,rad)
        x = sen[0] - rad
        y = sen[1]
        curr = []
        print("going up right")
        for d in range(rad): # up right
            x += d
            y += d
            curr.append((x,y))
        print("going down right")
        for d in range(rad): # down right
            x += d
            y -= d
            curr.append((x,y))
        print("going down left")
        for d in range(rad): # down left
            x -= d
            y -= d
            curr.append((x,y))
        print("going up left")
        for d in range(rad): # up left
            x -= d
            y += d
            curr.append((x,y))
        circles[sen] = curr
    return circles

def check_in_multiple(circles):
    interesting = set()
    for index, circle in circles.items():
        for coord in circle:
            print("checking new coord")
            for index2,circle2 in circles.items():
                if index != index2:
                    if coord in circle2:
                        interesting.add(coord)
    return interesting



if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        (sen, bea) = create_cave(lines)
        print(sen)
        print(bea)
        #show_cave(cave)        
        radii = get_radii(sen,bea)
        print(radii)
        #circles = circles_haha_not_at_all_circles(sen, radii)   # haha this crashes my python and terminal lol
        #interesting = check_in_multiple(circles)
        #print(interesting)
        print(max(radii))
