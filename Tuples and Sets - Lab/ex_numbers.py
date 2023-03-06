first_set = set(input().split(' '))
second_set = set(input().split(' '))
n = int(input())
for _ in range(n):
    command = input().split(' ')
    last_number = len(command)

    if command[0] == "Check" and command[1] == "Subset":
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

    if command[0] == 'Add' and command[1] == 'First':
        for number in range(2, last_number):
            numbers = command[number]
            if command[number] not in first_set:
                first_set.add(numbers)
    if command[0] == 'Add' and command[1] == 'Second':
        for number in range(2, last_number):
            numbers = command[number]
            if command[number] not in second_set:
                second_set.add(numbers)

    if command[0] == 'Remove' and command[1] == 'Second':
        for number in range(2, last_number):
            numbers = command[number]
            if numbers in second_set:
                second_set.remove(numbers)

    if command[0] == 'Remove' and command[1] == 'First':
        for number in range(2, last_number):
            numbers = command[number]
            if numbers in first_set:
                first_set.remove(numbers)


set1 = sorted(first_set)
set2 = sorted(second_set)
print(*set1, sep=", ")
print(*set2, sep=", ")
