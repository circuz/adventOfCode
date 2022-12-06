INPUT = "./day05_input"

def parse(lines):

    crates = {}
    print("asd")
    for i, line in enumerate(lines,1):
        if line[1] == "1":
            break
        for j in range(len(line)//4):
            if str(j+1) not in crates:
                crates[str(j+1)] = []
            thing = line[j*4 + 1]
            if thing.isalnum():
                crates[str(j+1)].insert(0,thing)
    print(crates)
    lines.readline() # empty line between " 1  2 ..." and "move x from x to x"
    print("==============================")

    for line in lines:
        [ number, locations ] = line.split("from")
        number = int(number.split("move")[1])
        [fro, to] = locations.split("to")
        to = to.split("\n")[0]
        to = to.strip()
        fro = fro.strip()
        for _ in range(number):
            print(f'crates: {crates}\n crates[fro]: {crates[fro]}')
            crates[to].append(crates[fro].pop())
            print(f'crates AFTER: {crates}\n\n')
    print(crates)
    
    result = ""
    for crate in crates:
        result += crates[crate][-1]

    return result
            

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        result = parse(lines)  
    print(result) 


