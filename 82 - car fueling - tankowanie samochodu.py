# 82 - car fueling - tankowanie samochodu
# Dana jest odległość, którą samochód musi pokonać na jednej drodze.
# Mamy również listę stacji benzynowych oraz całkowitą pojemność baku. Każda stacja
# jest zdefiniowana przez jej odległość od punktu 0, tzn. s to odległość między i-tą stacją
# a punktem 0. Znajdź algorytm, który obliczy minimalną liczbę tankowań (liczbę stacji,
# na których samochód musi się zatrzymać) na całej trasie. Samochód zaczyna z pełnym bakiem.

def car_fueling(distance, full_tank, stops):
    stops.sort()
    stops.append(distance)
    res = 0
    tank = full_tank
    current = 0
    for i in range(len(stops)):
        if stops[i] - current <= tank:
            tank -= stops[i] - current
            current = stops[i]
            continue
        res += 1
        tank = full_tank
        tank -= stops[i] - current
        if tank < 0: return False
        current = stops[i]
    return res

# Przykładowy test - oczekiwana wartość: 2
distance = 950
full_tank = 400
stops = [200, 375, 550, 750]
print(car_fueling(distance, full_tank, stops))\

# Przykładowy test - oczekiwana wartość: False
distance = 950
full_tank = 400
stops = [50, 600, 750]
print(car_fueling(distance, full_tank, stops))