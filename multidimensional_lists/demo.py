numbers_list = input().split(", ")
result = 0
for i in range(len(numbers_list)):
    number = int(numbers_list[i + 1])
    if number < 5:
        result *= number
    elif number > 5 and number > 10:
        result /= number
print(result)

