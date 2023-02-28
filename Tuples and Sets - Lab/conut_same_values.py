example = input().split(' ')
ss = {}
for ch in example:
    ch = float(ch)
    if ch in ss:
        ss[ch] += 1
    else:
        ss[ch] = 1

for number, count in ss.items():
    print(f'{number} - {count} times')
