length = int(input())
even_set = set()
odd_set = set()
current_score = 0

for line in range(1, length+1):
    name = input()
    for ch in name:
        current_score += ord(ch)
    current_sum = current_score // line
    if current_sum % 2 == 0:
        even_set.add(current_sum)
    else:
        odd_set.add(current_sum)
    current_score = 0

even_sum = sum(even_set)
odd_sum = sum(odd_set)

if even_sum == odd_sum:
    result = odd_set.union(even_set)
elif even_sum > odd_sum:
    result = odd_set.symmetric_difference(even_set)
else:
    result = odd_set.difference(even_set)

print(*result, sep=', ')