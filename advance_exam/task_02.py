size = int(input())
directions = input().split(', ')
matrix = []
squirrel_row, squirrel_col = None, None
hazelnuts = 0
outside = False
for _ in range(size):
    row = list(input())
    matrix.append(row)

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 's':
            squirrel_row, squirrel_col = row, col
trap = False


def is_outside(moves, rows, cols):
    is_outsides = False
    if moves == "up" and row < 0:
        is_outsides = True
    elif moves == "down" and rows == size:
        is_outsides = True
    elif moves == "left" and cols < 0:
        is_outsides = True
    elif moves == "right" and cols == size:
        is_outsides = True
    return is_outsides


def get_next_move(move, rows, cols):
    if move == "up":
        rows = rows - 1
    elif move == "right":
        cols = cols + 1
    elif move == "left":
        cols = cols - 1
    elif move == "down":
        rows = rows + 1
    return rows, cols


for direction in directions:

    squirrel_row, squirrel_col = get_next_move(direction, squirrel_row, squirrel_col)
    outside = is_outside(direction, squirrel_row, squirrel_col)
    if outside:
        print("The squirrel is out of the field.")
        break

    if matrix[squirrel_row][squirrel_col] == 'h':
        hazelnuts += 1
    elif matrix[squirrel_row][squirrel_col] == 't':
        trap = True
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    if hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break
    row, col = squirrel_row, squirrel_col
    matrix[row][col] = 's'

if hazelnuts < 3 and trap is False and outside is False:
    print("There are more hazelnuts to collect.")
print(f'Hazelnuts collected: {hazelnuts}')