from collections import deque

que = deque()

while True:
    command = input()
    if command == "Paid":
        for _ in range(len(que)):
            people = que.popleft()
            print(people)
    elif command == "End":
        break
    else:
        que.append(command)

print(f"{len(que)} people remaining.")