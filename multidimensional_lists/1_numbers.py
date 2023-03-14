first_set = set([int(x) for x in input().split()])
second_set = set([int(x) for x in input().split()])
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    if command[0] == 'Add':
        if command[1] == 'First':
            for ch in command:
                if ch.isdigit():
                    first_set.add(int(ch))
