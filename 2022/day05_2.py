INPUT = "./day05_input"

def parse(lines):

    crates = {}
    for i, line in enumerate(lines,1):
        if line[1] == "1":
            break
        for j in range(len(line)//4):
            if str(j+1) not in crates:
                crates[str(j+1)] = []
            thing = line[j*4 + 1]
            if thing.isalnum():
                crates[str(j+1)].insert(0,thing)
    lines.readline() # empty line between " 1  2 ..." and "move x from x to x"

    for line in lines:
        [ number, locations ] = line.split("from")
        number = int(number.split("move")[1])
        [fro, to] = locations.split("to")
        to = to.split("\n")[0]
        to = to.strip()
        fro = fro.strip()
        moving = crates[fro][-number:]
        for crate in moving:
            crates[fro].pop()
            crates[to].append(crate)
    
    result = ""
    for crate in crates:
        result += crates[crate][-1]

    return result
            

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        result = parse(lines)  
    print(result) 


