INPUT = "./day02_mini"
 
def score(lines):
    print(lines)
    throw_dict = { 'A': 1, 'B': 2, 'C':3, 'X': 1, 'Y': 2, 'Z': 3 }
    points = {0: 3, 1: 6, 2: 0}

    total = 0
    for line in lines:
        print(line)
        round_throws = line[:-1].split(" ")
        round_weights = [ throw_dict[throw] for throw in round_throws ]
        print(round_weights)
        print(round_throws)
        total += round_weights[1]
        total += points[(round_weights[1] - round_weights[0]) % 3]
        print(total)
    
    return total



if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        result = score(lines)      
    print(result)
