INPUT = "./day03_input"

def check(lines):
    result = 0
    lineabove = ""
    for i, line in enumerate(lines, 1):
        if not i % 3:
            for c in line:
                if (c in lineabove) and (c in lineaboveabove):
                    value = (ord(c) - 38) % 58
                    break
            result += value     
            continue
        lineaboveabove = lineabove
        lineabove = line
    print(result)

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        check(lines) 
        
