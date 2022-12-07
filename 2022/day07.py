INPUT = "./day07_input"

def count_sizes(lines):
    depth = 0
    total = 0
    tjoffabong = []
    for line in lines:
        args = line[:-1].split(" ")
        if args[1] == "cd":
            if args[2] == "..":
                if tjoffabong[depth-1] < 100000:
                    total += tjoffabong[depth-1]
                tjoffabong[depth-1] = 0
                depth -= 1
                continue
            else:
                depth += 1
                tjoffabong.append(0)
        if (args[0] != "$") and (args[0] != "dir"):
            tjoffabong = [tjoffabong[i] + int(args[0]) for i in range(depth)]
    if tjoffabong[depth-1] < 100000:
         total += tjoffabong[depth-1]
    print(total)

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        count_sizes(lines)
        # gå igenom alla rader och räkna ihop mellan en "cd x" och en "cd .."
        
