def next_moving(direction, rows, cols):
    if direction == "up":
        rows = rows - 1
    elif direction == "right":
        cols = cols + 1
    elif direction == "left":
        cols = cols - 1
    elif direction == "down":
        rows = rows + 1
    return rows, cols


def is_outside(direction, rows, cols):
    if direction == "up" and row < 0:
        rows = 5
    elif direction == "down" and rows > 5:
        rows = 0
    elif direction == "left" and cols < 0:
        cols = 5
    elif direction == "right" and cols > 5:
        cols = 0
    return rows, cols


water = 0
metal = 0
concrete = 0
matrix = []
rover_row, rover_col = None, None
for _ in range(6):
    matrix.append(input().split(' '))

for row in range(6):
    for col in range(6):
        if matrix[row][col] == "E":
            rover_row, rover_col = row, col
broken = False
commands = input().split(', ')
for command in commands:
    if broken:
        break
    rover_row, rover_col = next_moving(command, rover_row, rover_col)
    rover_row, rover_col = is_outside(command, rover_row, rover_col)

    if matrix[rover_row][rover_col] == "W":
        water += 1
        print(f"Water deposit found at ({rover_row}, {rover_col})")
    elif matrix[rover_row][rover_col] == "M":
        metal += 1
        print(f"Metal deposit found at ({rover_row}, {rover_col})")
    elif matrix[rover_row][rover_col] == "C":
        concrete += 1
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")
    elif matrix[rover_row][rover_col] == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        broken = True
        break
    matrix[rover_row][rover_col] = '-'

if water > 0 and metal > 0 and concrete > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

