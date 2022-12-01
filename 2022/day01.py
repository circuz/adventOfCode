INPUT = "./day01_input"

def make_dict(lines):
    elf = 0
    inventory = {elf: []}
    for line in lines:
        if line == "\n":
            elf += 1
            inventory[elf] = []
        else:
           inventory[elf].append(int(line))
    return inventory
 
if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        inventory = make_dict(lines)
    topthree = [0,0,0] 
    for elf in inventory:
        for one in topthree:
            if sum(inventory[elf]) > sum(inventory[one]):
                topthree.remove(one)
                topthree.append(elf)
                break
    carrying = [sum(inventory[elf]) for elf in topthree]
    print(sum(carrying))


