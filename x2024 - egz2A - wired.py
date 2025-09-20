# egzamin 2024 termin 2 zadanie 1 - wired
# Opis algorytmu - wired(T) - O(n^3):
# recur(w,k) - minimalny koszt przewodów pozwalających na połączenie wejść od w-tego do k-tego.
# Warunek końcowy rekurencji (k == w+1) - dwa wejścia tuż obok siebie można połączyć tylko na jeden sposób.
# Funkcja recur(w,k) dzieli przedział [w,k] na dwa przedziały [w,i-1] i [i,k] a następnie wybiera
# najbardziej optymalny podział. Rozważa również przypadek gdy indeks w-ty łączymy z k-tym a następnie
# oblicza recur(w+1,k-1).
# Wynik algorytmu to recur(0,len(T)-1).


from egz2atesty import runtests
from math import inf

def wired( T ):
    n = len(T)

    F = [[inf for k in range(n)] for w in range(n)]
    # F[w][k] - minimalny koszt przewodów pozwalających na połączenie wejść od w-tego do k-tego.

    def recur(w,k):
        if F[w][k] != inf:
            return F[w][k]
        if k == w+1:
            F[w][k] = 1 + abs(T[w]-T[k])
            return F[w][k]
        F[w][k] = recur(w+1,k-1) + 1 + abs(T[w]-T[k])
        for i in range(w+2,k,2):
            F[w][k] = min(
                F[w][k],
                recur(w,i-1) + recur(i,k)
            )
        return F[w][k]

    return recur(0,n-1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = True )
