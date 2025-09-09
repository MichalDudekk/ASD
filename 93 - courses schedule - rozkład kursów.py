# 93 - courses schedule - rozkład kursów
# Istnieje n różnych kursów online o numerach od 1 do n. Dana jest tablica courses,
# gdzie courses[i] = [czas_trwania_i, ostatni_dzień_i] wskazuje, że i-ty kurs
# powinien być prowadzony nieprzerwanie przez czas_trwania_i dni i musi zostać
# zakończony przed lub w ostatni_dzień_i.
# Zaczynasz pierwszego dnia i nie możesz brać dwóch lub więcej kursów jednocześnie.
# Zwróć maksymalną liczbę kursów, które możesz wziąć.

import heapq

def scheduleCourse(courses):
    res = 0
    current = 0
    max_heap = []
    courses.sort(key=lambda x:x[1])
    for i in range(len(courses)):
        if current + courses[i][0] <= courses[i][1]:
            heapq.heappush(max_heap,-courses[i][0])
            current += courses[i][0]
            res += 1
            continue
        if not max_heap:
            continue
        if courses[i][0] < -max_heap[0]:
            current -= -heapq.heappop(max_heap) - courses[i][0]
            heapq.heappush(max_heap,-courses[i][0])
    return res

# Przykładowy test - oczekiwana wartość: 3
courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
print(scheduleCourse(courses))
# Przykładowy test - oczekiwana wartość: 5
courses = [[100,200],[200,1500],[1000,1250],[300,3300],[1000,1200],[1700,3000]]
print(scheduleCourse(courses))