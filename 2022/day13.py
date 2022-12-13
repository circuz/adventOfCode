INPUT = "./day13_input"
# 1093 too low :(

def create_pairs(lines):
    pairs = {1: []}
    index = 1
    for line in lines:
        if line == "\n":
            index += 1
            pairs[index] = []
            continue
        pairs[index].append(eval(line))
    return pairs

def which_sorted(pair_dict):
    sorted_pairs = []
    for index,pair in pair_dict.items():
        print(index,pair)
        if is_sorted(pair[0], pair[1]):
            sorted_pairs.append(index)
    return sorted_pairs
 
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

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        pairs = create_pairs(lines) 
        print(pairs)
        sorted_pairs = which_sorted(pairs)
        print(sorted_pairs)
        print(f'Sum is {sum(sorted_pairs)}')
