INPUT = "./day03_input"

def check(lines):
    result = 0
    for line in lines:
        first = line[:len(line)//2] 
        second = line[len(line)//2:] 
        for c in first:
            if c in second:
                value = (ord(c) - 38) % 58
                break
        result += value     
    print(result)

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        check(lines) 
        
