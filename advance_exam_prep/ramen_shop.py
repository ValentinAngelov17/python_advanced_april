from collections import deque
bowl_of_ramen = [int(x) for x in input().split(', ')]
customers = deque(int(x) for x in input().split(', '))

while bowl_of_ramen and customers:
    ramen = bowl_of_ramen.pop()
    customer = customers.popleft()
    if ramen == customer:
        continue
    elif ramen > customer:
        ramen -= customer
        bowl_of_ramen.append(ramen)
    elif customer > ramen:
        customer -= ramen
        customers.appendleft(customer)

if len(customers) == 0:
    print('Great job! You served all the customers.')
    if bowl_of_ramen:
        left_bows = ', '.join(str(x) for x in bowl_of_ramen)
        print(f"Bowls of ramen left: {left_bows}")
elif len(bowl_of_ramen) == 0:
    print("Out of ramen! You didn't manage to serve all customers.")
    left_customers = ', '.join(str(x) for x in customers)
    print(f"Customers left: {left_customers}")
