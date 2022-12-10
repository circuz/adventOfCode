INPUT = "./day10_input"

def get_signal_strengths(lines):
    X = [1]
    for i,line in enumerate(lines):
        X.append(X[-1])
        args = line[:-1].split(" ")
        if args[0] == "addx":
            X.append( X[-1] + int(args[1]))
    return X

def sum_interesting_signals(array):
    i = 19
    interesting = []
    while i < len(array):
        interesting.append(array[i]*(i+1))
        i += 40
    return sum(interesting)

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        X = get_signal_strengths(lines) 
        signal_sum = sum_interesting_signals(X)
        print(signal_sum)
