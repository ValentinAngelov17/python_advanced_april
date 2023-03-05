length = int(input())
first_set = set()
second_set = set()
best_solution = set()
list_result = []

for _ in range(length):
    text = input().split('-')
    first = text[0].split(',')
    second = text[1].split(',')
    first_start = int(first[0])
    first_end = int(first[1])
    second_start = int(second[0])
    second_end = int(second[1])
    for number in range(first_start, first_end +1):
        first_set.add(number)
    for number in range(second_start, second_end +1):
        second_set.add(number)
    result = first_set.intersection(second_set)
    if len(result) > len(best_solution):
        best_solution = result
    first_set = set()
    second_set = set()
for numbers in best_solution:
    list_result.append(numbers)
print(f'Longest intersection is {list_result} with length {len(best_solution)}')



