INPUT = "./day08_input"
# mini ska bli 21

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

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        matrix, matrix_t = build_matrices(lines)
        visible_matrix = check_visible(matrix, matrix_t)
        total = sum([ sum(row) for row in visible_matrix ]) 
        print(total)
