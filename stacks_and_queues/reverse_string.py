command = input()
s = []
for c in command:
    s.append(c)

reverse_string = []
for i in range(len(s)):
    last = s.pop()
    reverse_string.append(last)
print("".join(reverse_string))