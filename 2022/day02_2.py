INPUT = "./day02_input"
 
def score(lines, score_dict):
    total = 0
    for line in lines:
        round_throws = line[:-1].split(" ")
        total += score_dict[round_throws[0]][round_throws[1]] 
    return total

def build_dict():
    score_dict = {
        "A": { "X": 3, "Y": 4, "Z": 8 },
        "B": { "X": 1, "Y": 5, "Z": 9 },
        "C": { "X": 2, "Y": 6, "Z": 7 }}
    return score_dict


if __name__ == "__main__":
    score_dict = build_dict()
    with open(INPUT,'r') as lines:
        result = score(lines, score_dict)      
    print(result)
