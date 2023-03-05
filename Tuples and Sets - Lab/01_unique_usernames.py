n = int(input())
people = set()

for _ in range(n):
    username = input()
    people.add(username)

for person in people:
    print(person)