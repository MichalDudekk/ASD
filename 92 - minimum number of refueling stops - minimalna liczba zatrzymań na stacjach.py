# 92 - minimum number of refueling stops - minimalna liczba zatrzymań na stacjach
# Samochód jedzie z pozycji początkowej do celu, który znajduje się target mil na wschód od pozycji początkowej.
# Na drodze znajdują się stacje benzynowe. Stacje benzynowe są reprezentowane jako tablica stations,
# gdzie stations[i] = [pozycja_i, paliwo_i] oznacza, że i-ta stacja benzynowa znajduje się pozycja_i mil na
# wschód od pozycji początkowej i ma paliwo_i litrów paliwa.
# Samochód startuje z nieskończonym bakiem paliwa, który początkowo ma startFuel litrów paliwa.
# Zużywa jeden litr paliwa na każdą przejechaną milę. Kiedy samochód dotrze do stacji benzynowej,
# może się zatrzymać i zatankować, przenosząc całe paliwo ze stacji do samochodu.
# Zwróć minimalną liczbę postojów na tankowanie, które samochód musi wykonać, aby dotrzeć do celu.
# Jeśli nie może dotrzeć do celu, zwróć -1.

from queue import PriorityQueue

def minRefuelStops(target, startFuel, stations):
    tank = startFuel
    position = 0
    res = 0
    stations.append( (target,0) )
    pq = PriorityQueue()
    for i in range(len(stations)):
        l = stations[i][0] - position
        while l > tank:
            if pq.empty():
                return -1
            tank += -1*pq.get()
            res += 1
        tank -= l
        position = stations[i][0]
        pq.put( -1*stations[i][1] )
    return res

# Przykładowy test - oczekiwana wartość: 0
target = 1
startFuel = 1
stations = []
print(minRefuelStops(target, startFuel, stations))
# Przykładowy test - oczekiwana wartość: -1
target = 100
startFuel = 1
stations = [[10,100]]
print(minRefuelStops(target, startFuel, stations))
# Przykładowy test - oczekiwana wartość: 2
target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]
print(minRefuelStops(target, startFuel, stations))
# Przykładowy test - oczekiwana wartość: 1
target = 100
startFuel = 50
stations = [[25,50],[50,25]]
print(minRefuelStops(target, startFuel, stations))
