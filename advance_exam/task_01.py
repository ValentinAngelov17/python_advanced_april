from collections import deque
programmers_time = deque(int(x) for x in input().split(' '))
number_of_tasks = [int(x) for x in input().split(' ')]
darth_vader_ducky = 0
thor_ducky = 0
big_blue_ducky = 0
small_yellow_ducky = 0

while programmers_time and number_of_tasks:
    p_time = programmers_time.popleft()
    tasks = number_of_tasks.pop()
    temp_sum = p_time * tasks

    if  0 <= temp_sum <= 60:
        darth_vader_ducky += 1
    elif 61 <= temp_sum <= 120:
        thor_ducky += 1
    elif 121 <= temp_sum <= 180:
        big_blue_ducky += 1
    elif 181 <= temp_sum <= 240:
        small_yellow_ducky += 1
    elif temp_sum >= 241:
        programmers_time.append(p_time)
        tasks -= 2
        number_of_tasks.append(tasks)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {darth_vader_ducky}")
print(f"Thor Ducky: {thor_ducky}")
print(f"Big Blue Rubber Ducky: {big_blue_ducky}")
print(f"Small Yellow Rubber Ducky: {small_yellow_ducky}")
