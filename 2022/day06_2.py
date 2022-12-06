INPUT = "./day06_input"

def is_start(chars):
    for c in chars:
        if chars.count(c) > 1:
            return False
    return True

def search_start(lines):
    pos = 0
    first = True
    prev = ""
    for line in lines:
        length = len(line) - 1
        if first:
            first = False
            for i in range(14,length):
                if is_start(line[i-14:i]):
                    print(line[i-14:i])
                    return i
        else:
            for i in range(length):
                if i < 14:
                    if is_start(prev[-14 + i:] + line[0:i]):
                        print(prev[-14 + i:] + line[0:i])
                        return pos + i
                else:
                    if is_start(line[i-14:i]):
                        print(line[i-14:i])
                        return pos + i

        prev = line[-15:-1]
        pos += length


if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        result = search_start(lines)
    print(result)
