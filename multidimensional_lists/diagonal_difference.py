n = int(input())
matrix = []
primary_diagonal =[]
secondary_diagonal = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])
for i in range(n):
    primary_diagonal.append(matrix[i][i])

for j in range(n):
    secondary_diagonal.append(matrix[j][n -1])
    n = n-1

a = sum(primary_diagonal)
b = sum(secondary_diagonal)
print(abs(a - b))