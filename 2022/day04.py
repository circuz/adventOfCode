INPUT = "./day04_input"

def reduntant(line):
    [a, b] = line.split(",")
    [alo, ahi] = a.split("-")
    [blo, bhi] = b.split("-")
    alo = int(alo)
    ahi = int(ahi)
    blo = int(blo)
    bhi = int(bhi)

    return ( alo >= blo and ahi <= bhi ) or ( alo <= blo and ahi >= bhi )

def check_lines(lines):
    result = 0
    for line in lines:
        result += reduntant(line)
    return result

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        total = check_lines(lines)
    print(total)
        
