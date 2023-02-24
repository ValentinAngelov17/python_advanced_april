from collections import deque

water_quantity = int(input())
people_queue = deque()

while True:
    command = input()
    if command == 'Start':
        break
    else:
        people_queue.append(command)

while True:
    command = input()
    if command == "End":
        print(f'{water_quantity} liters left')
        break
    elif command.startswith("refill "):
        split_command = command.split(' ')
        refill = int(split_command[1])
        water_quantity += refill
    else:
        if int(command) <= water_quantity:
            water_quantity -= int(command)
            current_people = people_queue.popleft()
            print(f'{current_people} got water')
        else:
            current_people = people_queue.popleft()
            print(f'{current_people} must wait')

