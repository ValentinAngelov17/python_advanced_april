n = input().split(", ")
m = int(n[0])
matrix = []

sum_elements = 0
for i in range(m):
    numbers = [int(x) for x in input().split(", ")]
    matrix.append(numbers)
    sum_elements += sum(matrix[i])


print(sum_elements)
print(matrix)
