text = input()
letters_dict = {}
for ch in text:
    if ch in letters_dict:
        letters_dict[ch] += 1
    else:
        letters_dict[ch] = 1

for key, value in sorted(letters_dict.items()):
    print(f'{key}: {value} time/s')