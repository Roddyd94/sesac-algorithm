n = int(input())

cars = {}

for i in range(n):
    car_id = input()
    cars[car_id] = i

pasing_car_indices = []
for i in range(n):
    lag = 0
    car_id = input()
    car_ix = cars[car_id]

    for pass_ix in pasing_car_indices:
        if car_ix < pass_ix:
            lag += 1

    if car_ix + lag > i:
        pasing_car_indices.append(cars[car_id])


print(len(pasing_car_indices))
