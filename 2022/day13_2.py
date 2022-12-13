INPUT = "./day13_input"

def get_packets(lines):
    packets = []
    for line in lines:
        if line != "\n":
            packets.append(eval(line))
    return packets

def is_sorted(a,b):
    diff = len(a)-len(b)
    a += [-1] * -diff
    b += [-1] * diff
    #print(a,b)
    value = [-1,-1]
    for values in zip(a,b):
        value[0] = values[0]
        value[1] = values[1]
        if type(value[0]) == list or type(value[1]) == list:
            if type(value[1]) != list:
                if value[1] == -1:
                    return False
                value[1] = [value[1]]
            if type(value[0]) != list:
                if value[1] == -1:
                    return False
                value[0] = [value[0]]
            if not is_sorted(value[0],value[1]):
                return False
            if is_sorted(value[0],value[1]) == "Very True":
                return "Very True"
        else:
            if value[0] > value[1]:
                return False
            if value[0] < value[1]:
                return "Very True"
    return True

def sort_that_bad_boy(packets):
    sorted_list = [[[2]],[[6]]]
    for packet in packets:
        #print(packet)
        sploink = False
        for i,sorted_item in enumerate(sorted_list):
            if is_sorted(packet,sorted_item):
                sorted_list.insert(i,packet)
                sploink = True
                break
        if sploink == False:
            sorted_list.append(packet)
    return sorted_list

def clean(packet):
    #print(f'Before: {packet}')
    while -1 in packet:
        packet.remove(-1)
    for value in packet:
        if type(value) == list:
            packet = clean(value)
    #print(packet)
    return packet

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        packets = get_packets(lines) 
        #print(packets)
        sorted_packets = sort_that_bad_boy(packets)
        #print("===========")
        clean(sorted_packets)
        #print(clean(sorted_packets))
        #print(sorted_packets)
        print(sorted_packets.index([[2]])+1)
        print(sorted_packets.index([[6]])+1)
        print((sorted_packets.index([[2]])+1)*(sorted_packets.index([[6]])+1))
        #sorted_pairs = which_sorted(pairs)
        #print(sorted_pairs)
        #print(f'Sum is {sum(sorted_pairs)}')
