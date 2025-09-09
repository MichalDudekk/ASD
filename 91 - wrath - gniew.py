# 91 - wrath - gniew
# W kolejce stoi n winnych ludzi, i-ty z nich trzyma pazur o długości L[i]. Dzwoni dzwonek
# i każda osoba zabija część ludzi stojących przed nią. Wszyscy zabijają innych jednocześnie.
# Mianowicie, i-ta osoba zabija j-tą osobę wtedy i tylko wtedy, gdy j < i i j >= i-L[i].
# Dane są długości pazurów. Musimy znaleźć całkowitą liczbę żywych ludzi po dzwonku.

def wrath(L):
    n = len(L)
    alive = 0
    death_pointer = n
    for i in range(n-1,-1,-1):
        if i < death_pointer:
            alive += 1
        death_pointer = min(death_pointer,i-L[i])
    return alive

# Przykładowy test - oczekiwana wartość: 4
L = [1, 0, 0, 1, 1, 3, 2, 0, 0, 2, 3]
print(wrath(L))