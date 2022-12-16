INPUT = "./day16_input"


class Network():
    def __init__(self):
        self._minutes = 30
        self._current = "AA"
        self._tunnels = {}
        self._valves = {}

    def move_to(self,name):
        self._current = name
        self._minutes -= 1
        return

    def add_valve(self, name, flow_rate, tunnels):
        self._valves[name] = flow_rate
        self._tunnels[name] = {valve:1 for valve in tunnels}
        return

def createnetwork(lines):
    net = Network()
    for line in lines:
        name = line[6:9]
        flow_rate = int(line.split("flow rate=")[1].split(";")[0])
        tunnels = line.split(" ")[:-1][9:]
        net.add_valve(name, flow_rate, tunnels)

    nzn = Network()
    print(net._valves)
    print(net._tunnels)

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        createnetwork(lines)
        
