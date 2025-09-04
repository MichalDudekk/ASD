# 86 - machines saving people - maszyny ratujące ludzi
# W jednej z chińskich prowincji postanowiono zbudować serię maszyn chroniących
# ludność przed koronawirusem. Prowincję można wizualizować jako tablicę wartości 1 i 0,
# gdzie arr[i] = 1 oznacza, że w mieście [i] można zbudować maszynę, a wartość 0, że nie.
# Istnieje również liczba k, która oznacza, że jeśli postawimy maszynę w mieście [i],
# to miasta o indeksach [j] takich, że abs(i-j) < k są przez nią chronione.
# Znajdź minimalną liczbę maszyn potrzebnych do zapewnienia bezpieczeństwa w każdym
# mieście, lub -1, jeśli jest to niemożliwe.

def machines_saving_people(T, k):
    counter = 0
    unguarded = 0
    last = None
    i = 0
    while i < len(T):
        if abs(unguarded - i) >= k:
            if last is None:
                return -1
            counter += 1
            i = last + k
            unguarded = last + k
            last = None
        if T[i] == 1:
            last = i
        i += 1

    if unguarded < len(T):
        for j in range(unguarded,max(0,unguarded-k),-1):
            if T[j] == 1:
                counter += 1
                return counter
        return -1
    return counter

# Przykładowy test - oczekiwana wartość: 3
T = [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
k = 4
print(machines_saving_people(T, k))
# Przykładowy test - oczekiwana wartość: -1
T = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
k = 4
print(machines_saving_people(T, k))