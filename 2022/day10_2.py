INPUT = "./day10_input"

def get_signal_strengths(lines):
    X = [1]
    for i,line in enumerate(lines):
        X.append(X[-1])
        args = line[:-1].split(" ")
        if args[0] == "addx":
            X.append( X[-1] + int(args[1]))
    return X

def render(positions):
    
    for i, X in enumerate(positions):
        if abs((i%40)-X) <= 1:
            print('#',end="")
        else:
            print('.',end="")
        if i % 40 == 39:
            print("")

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        X = get_signal_strengths(lines) 
        render(X)
