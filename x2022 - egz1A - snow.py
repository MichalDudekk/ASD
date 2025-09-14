# egzamin 2022 termin 1 zadanie 1 - snow

from egz1atesty import runtests

# O(n)
def snow( S ):
    def count_sort(T):
        n = len(T)
        maxi = max(T)
        num = [0 for _ in range(maxi+1)]
        m = len(num)
        for i in range(n):
            num[T[i]] += 1
        for i in range(1,m):
            num[i] = num[i-1] + num[i]
        new = [0 for _ in range(n)]
        for i in range(n-1,-1,-1):
            num[T[i]] -= 1
            new[num[T[i]]] = T[i]
        return new

    n = len(S)
    time = 0
    res = 0
    new = []
    for i in S:
        if i >= n:
            res += i - time
            time += 1
        else:
            new.append(i)

    new = count_sort(new)
    new.reverse()

    for i in range(n):
        height = new[i] - time
        if height <= 0:
            break
        res += height
        time += 1
    return res

# O(n*log(n))
def snow_( S ):
    n = len(S)
    S.sort(reverse = True)
    res = 0
    time = 0
    for i in range(n):
        height = S[i] - time
        if height <= 0:
            break
        res += height
        time += 1
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )

# Liczba zaliczonych testów: 10/10
# Liczba testów z przekroczonym czasem: 0/10
# Liczba testów z błędnym wynikiem: 0/10
# Liczba testów zakończonych wyjątkiem: 0/10
# Orientacyjny łączny czas : 1.20 sek.
# Status testów: A A A A A A A A A A