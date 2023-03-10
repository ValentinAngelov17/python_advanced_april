n = int(input())
matrix = []

def primary_diagonal_sum(matrix):
    for _ in range(n):
        numbers = [int(x) for x in input().split()]
        matrix.append(numbers)

    return sum(matrix[i][i] for i in range(n))

print(primary_diagonal_sum(matrix))

