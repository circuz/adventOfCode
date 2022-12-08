INPUT = "./day08_input"
# mini ska bli 8
# 5661 too low

def build_matrices(lines):
    matrix = []
    for line in lines:
        line = line[:-1]
        matrix.append([])
        for n in line:
            matrix[-1].append(int(n))
    matrix_t = [ [] for col in matrix[0] ]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            matrix_t[i].append(matrix[j][i])
    return matrix, matrix_t

def check_visible_rows(check_matrix):
    visible_matrix = []
    #print(check_matrix)
    for row in check_matrix:
        row_visible = []
        lo = 0
        tallest = -1
        for i, n in enumerate(row):
            if n > tallest:
                tallest = n
                row_visible.append(1)
                continue
            row_visible.append(0)
        old_tallest = tallest
        tallest = -1
        while i > 0:
            if row[i] > tallest:
                tallest = row[i]
                row_visible[i] = 1
            i -= 1
        visible_matrix.append(row_visible)
    return visible_matrix

def check_visible(matrix, matrix_t):
    visible_row = check_visible_rows(matrix)
    #print(visible_row)
    visible_col = check_visible_rows(matrix_t)
    #print(visible_col)
    visible = []
    for i in range(len(matrix)):
        visible.append([])
        for j in range(len(matrix[0])):
           visible[i].append(visible_row[i][j] or visible_col[j][i]) 
    #print(visible)
    return visible

def check_score(mat, x, y):
    #print(mat, x, y, mat[y][x])
    height = mat[y][x]
    up = 0
    down = 0
    left = 0
    right = 0
    B = y - 1
    # check up
    while True:
        B -= 1
        up += 1
        if B == -1 or mat[B+1][x] >= height:
            break
    B = y + 1
    # check down
    while True:
        B += 1
        down += 1
        if B == len(mat) or mat[B-1][x] >= height:
            break
    A = x - 1
    # check left
    while True:
        A -= 1
        left += 1 
        if A == -1 or mat[y][A+1] >= height:
            break
    A = x + 1
    # check right
    while True:
        A += 1
        right += 1
        if A == (len(mat[0])) or mat[y][A-1] >= height:
            break
   #print(f'up: {up}')
   #print(f'donw: {down}')
   #print(f'left: {left}')
   #print(f'right: {right}')
    return up * down * left * right

def get_score(visible, mat):
    score = -1
    #print(visible)
    for j in range(1,len(mat)-1):
        for i in range(1,len(mat[0])-1):
            if visible[j][i]:
                score = max(score, check_score(mat, i, j))
    return score


if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        matrix, matrix_t = build_matrices(lines)
        visible_matrix = check_visible(matrix, matrix_t)
        max_scenic_score = get_score(visible_matrix, matrix)
        print(max_scenic_score)
