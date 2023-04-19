from collections import deque

textiles = deque([int(x) for x in input().split(' ')])
medicaments = [int(x) for x in input().split(' ')]
patch_counter = 0
bandage_counter = 0
medkit_counter = 0

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    if (textile + medicament) == 30:
        patch_counter += 1
    elif (textile + medicament) == 40:
        bandage_counter += 1
    elif (textile + medicament) == 100:
        medkit_counter += 1
    elif (textile + medicament) < 100 and (textile + medicament) != 30 and (textile + medicament)!= 40 and (textile + medicament) != 100:
        medicament += 10
        medicaments.append(medicament)

    if (textile + medicament) > 100:
        medkit_counter += 1
        remaining = (textile + medicament) - 100
        medicaments[-1] += remaining


if not textiles:
    print("Textiles are empty.")
else:
    print("Medicaments are empty.")

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")


