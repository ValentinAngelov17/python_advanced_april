from collections import deque
food_portion = [int(x) for x in input().split(', ')]
stamina_deque = deque(int(x) for x in input().split(', '))
mountain_peaks = {'Vihren': 80, 'Kutelo': 90, 'Banski Suhodol': 100, 'Polezhan': 60, 'Kamenitza':70}
conquered_mountains = []
day = 1

for mountain, needed_value in mountain_peaks.items():
    if day > 7 or len(conquered_mountains) == 5 or len(food_portion) == 0 or len(stamina_deque) == 0:
        break
    if food_portion and stamina_deque and mountain_peaks:
        food = food_portion.pop()
        stamina = stamina_deque.popleft()
        summary = food + stamina
        if summary >= needed_value:
            conquered_mountains.append(mountain)
            day += 1
        else:
            mountain_peaks[0] = mountain_peaks[mountain]
            day += 1


if len(conquered_mountains) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_mountains:
    print("Conquered peaks:")
    for x in conquered_mountains:
        print(x)

