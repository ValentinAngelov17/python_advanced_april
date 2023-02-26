clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
rack_counter = 1
current_rack_capacity = rack_capacity
while clothes:
   piece_of_clothing = clothes[-1]
   if piece_of_clothing > current_rack_capacity:
       rack_counter += 1
       current_rack_capacity = rack_capacity
   else:
       current_rack_capacity -= piece_of_clothing
       clothes.pop()

print(rack_counter)