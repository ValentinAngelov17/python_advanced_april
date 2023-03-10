from collections import deque

words = deque(input().split())

primary_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

collected_colors = []

while words:
    left = words.popleft()
    right = words.pop() if words else ""

    result = left + right
    if result in primary_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    result = right + left
    if result in primary_colors or result in secondary_colors:
        collected_colors.append(result)
        continue
    left = left[:-1]
    right = right[:-1]

    if left:
        words.insert(len(words) // 2, left)
    if right:
        words.insert(len(words) // 2, right)

print(collected_colors)
