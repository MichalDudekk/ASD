# egzamin 2024 termin 1 zadanie 2 - kstrong
# Opis algorytmu - kstrong(T, k) - O(nk):
# F[w][kol] - maksymalna suma podciągu z elementów od T[0] do T[kol] po usunięciu dokładnie kol elementów.
# Dla każdego i-tego indeksu w T przypisuje wartości początkowe F[0][i] = T[i] oraz F[1][i] = 0, aby
# algorytm rozważył rozpoczęcie ciągu na każdym indeksie.
# Algorytm przechodzi po każdym wierszu w i-tej kolumnie i wypełnia i+1-szą kolumne. Rozważa:
# - wzięcie i+1-szej wartości do sumy
# - nie wzięcie i+1-szej wartości do sumy
# W ten sposób algorytm rozważa wszystkie możliwe sumy. Aby odczytać wynik należy przejść po całej
# tablicy F (wynikowa suma może zaczynać się na dowolnym indeksie) i wybrać z niej największą wartość.

from egz1btesty import runtests
from math import inf

# O(n^3 * log(n))
def kstrong_worst(T,k):
    n = len(T)
    res = -inf

    for i in range(n):
        for l in range(0,n-i):
            array = T[i:i+l+1]
            array.sort()
            sum_array = sum(array)
            for j in range(k):
                if j >= len(array):
                    break
                if array[j] >= 0:
                    break
                sum_array -= array[j]
            res = max(res,sum_array)
    return res


# O(nk)
def kstrong( T, k):
    n = len(T)

    F = [[-inf for kol in range(n)] for w in range(k+1)]
    # F[w][kol] - maksymalna suma podciągu z elementów od T[0] do T[kol] po usunięciu dokładnie kol elementów
    for kol in range(n):
        F[0][kol] = T[kol]
        F[1][kol] = 0

    for kol in range(n-1):
        for w in range(k+1):
            if F[w][kol] == -inf:
                continue
            F[w][kol+1] = max( F[w][kol+1] , F[w][kol] + T[kol+1] ) # biorę kol+1-szy element
            if w+1 <= k:
                F[w+1][kol+1] = max( F[w+1][kol+1] , F[w][kol] )    # nie biorę kol+1-szego elementu

    res = -inf
    for kol in range(n):
        for w in range(k+1):
            res = max(res,F[w][kol])
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )

# Liczba zaliczonych testów: 11/11
# Liczba testów z przekroczonym czasem: 0/11
# Liczba testów z błędnym wynikiem: 0/11
# Liczba testów zakończonych wyjątkiem: 0/11
# Orientacyjny łączny czas : 1.78 sek.
# Status testów: A A A A A A A A A A A