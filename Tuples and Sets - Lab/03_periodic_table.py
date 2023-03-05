n = int(input())
chemical_set = set()

for _ in range(n):
    elements = input().split()
    for el in elements:
        chemical_set.add(el)
for element in chemical_set:
    print(element)