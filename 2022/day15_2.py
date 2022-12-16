import matplotlib.pyplot as plt
# 9814447029623 too low
# not 12118494453611 either
# try around 2453611, 3029623
# OK I FOUND IT BY PLAYING AROUND WITH CODE I CAN'T EXPLAIN IT!
# basically look at "circles" 6 and 10, and 20 and 19. they are 1 apart.
# they cross at 2740279, 2625406
TESTX = 2453611
TESTY = 3029623

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

def get_extremes(sensors, radii):
    circles = {}
    i = 0
    for sen in sensors:
        # circle = [ right, up, left, down ]
        circles[i+1] = [ (sen[0] + radii[i], sen[1]),(sen[0], sen[1] - radii[i]),(sen[0] - radii[i], sen[1]),(sen[0], sen[1] + radii[i]), ]
        i += 1
    return circles 

def top_right_pair(circles):
    """ where would a line from a to b cross 0? It would cross at x - y as we have lines f(x) = y. so look for circles such that the top is two more than anothers bot """
    pairs = {} 
    for i,circle1 in circles.items():
        pairs[i] = []
        topoffset = circle1[1][0] - circle1[1][1]
        for j, circle2 in circles.items():
            if circle2[3][0] - circle2[3][1] == topoffset - 2:
                pairs[i].append(j)
    return pairs


def top_left_pair(circles):
    """ where would a line from a to b cross 0? It would cross at x + y as we have lines f(x) = y. so look for circles such that the top is two less than anothers bot """
    pairs = {} 
    for i,circle1 in circles.items():
        pairs[i] = []
        topoffset = circle1[1][0] + circle1[1][1]
        for j, circle2 in circles.items():
            if circle2[3][0] + circle2[3][1] == topoffset - 2:
                print("ASD")
                pairs[i].append(j)
    return pairs


def show_circles(circles):
    for i,circle in circles.items():
        """
        if i != 10:
            if i != 6:
                continue
                """
        """
        if i != 20:
            if i != 19:
                continue
                """
        plt.plot([circle[0][0], circle[1][0], circle[2][0], circle[3][0], circle[0][0]], [circle[0][1], circle[1][1], circle[2][1], circle[3][1], circle[0][1], ])
    plt.plot([0,0,4000000,4000000,0],[0,4000000,4000000,0,0])
    plt.plot([0,4000000,],[0,4000000])
    #plt.plot([0,0,20,20,0],[0,20,20,0,0])
    plt.show()

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        (sen, bea) = create_cave(lines)
        print(sen)
        print(bea)
        radii = get_radii(sen,bea)
        print(radii)
        circles = get_extremes(sen,radii)
        print(circles)
        show_circles(circles)
        pairs = top_right_pair(circles)
        pairs2 = top_left_pair(circles)
        print(pairs)
        print(pairs2)

