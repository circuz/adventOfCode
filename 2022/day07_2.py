INPUT = "./day07_input"

def count_sizes(lines):
    to_remove = 1735494
    #to_remove = 8381165
    depth = 0
    total = 0
    tjoffabong = []
    folder = []
    best = {"name": "asd", "size": 9999999999999999999}
    outer = 0
    for line in lines:
        #print(line)
        args = line[:-1].split(" ")
        if args[1] == "cd":
            if args[2] == "..":
                if tjoffabong[depth-1] > to_remove:
                    if tjoffabong[depth-1] < best["size"]:
                        best["name"] = folder[-1]
                        best["size"] = tjoffabong[depth-1]
                        print(best)
                        print("AAAAAAAAAAAAAAAA")
                    total += tjoffabong[depth-1]
                #folder[depth-1] = 0
                folder.pop()
                depth -= 1
                temp = tjoffabong.pop()
                tjoffabong[-1] += temp
            else:
                depth += 1
                folder.append(args[2])
                tjoffabong.append(0)
        if (args[0] != "$") and (args[0] != "dir"):
            if depth == 1:
                outer += int(args[0])
            #tjoffabong = [tjoffabong[i] + int(args[0]) for i in range(depth)]
            tjoffabong[-1] += int(args[0])
            #folder = [folder[i] for i in range(depth)]
        print(outer)
        print(tjoffabong)
        print(folder)
    if tjoffabong[depth-1] < 100000:
         total += tjoffabong[depth-1]
    print(tjoffabong)
    to_remove = 30000000 - (70000000 - sum(tjoffabong) )
    print(to_remove)
    print(best)

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        count_sizes(lines)
        # gå igenom alla rader och räkna ihop mellan en "cd x" och en "cd .."
        
