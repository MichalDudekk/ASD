# 15 - subset sum - suma podzbiorów
# Dany jest zbiór liczb nieujemnych oraz wartość sumy. Sprawdź, czy istnieje podzbiór tego zbioru,
# którego suma elementów jest równa podanej sumie.
# Opis algorytmu na dole.

# zapamiętywanie za pomocą słownika - O(n*target)
def subset_sum(T,target):
    n = len(T)
    possible = {}
    possible[0] = True

    for i in range(n):
        new = []
        for sub_sum in possible.keys():
            new_sum = T[i]+sub_sum
            if new_sum == target:
                return True
            if new_sum > target:
                continue
            new.append(new_sum)
        for n in new:
            possible[n] = True
    return False

# bottom up - O(n*target)
def subset_sum_dp(T,target):
    n = len(T)
    F = [False for _ in range(target+1)]
    # F[s] - czy da się osiągnąć sumę s
    F[0] = True

    for i in range(n):
        for sub_sum in range(target,T[i]-1,-1):     # musimy iterować od tyłu, bo inaczej T[i] mogłoby zostać użyte kilka razy
            if F[sub_sum - T[i]]:
                F[sub_sum] = True
                if sub_sum == target:
                    return True
    return False

# Ciekawostka - algorytm z użyciem masek bitowych - O(n)
def subset_sum_bitmask(T, target):
    mask = 1  # Reprezentuje sumę 0
    for num in T:
        mask |= (mask << num)       # Przesuwamy maskę o num bitów w lewo i wykonujemy OR
        if (mask >> target) & 1:    # Sprawdzamy czy target jest osiągalny
            return True
    return False


D = [14, 5, 19, 3, 20, 14, 12, 7, 1]
# Przykładowy test - oczekiwana wartość: True
summary = 18
print(subset_sum(D, summary))
print(subset_sum_dp(D, summary))
print(subset_sum_bitmask(D, summary))
# Przykładowy test - oczekiwana wartość: True
summary = 92
print(subset_sum(D, summary))
print(subset_sum_dp(D, summary))
print(subset_sum_bitmask(D, summary))
# Przykładowy test - oczekiwana wartość: False
summary = 93
print(subset_sum(D, summary))
print(subset_sum_dp(D, summary))
print(subset_sum_bitmask(D, summary))

# Opis algorytmu - subset_sum_dp(T,target) - O(n*target)
# F[s] - czy da się osiągnąć sumę s
# Dla każdej liczby T[i] iterujemy od tyłu po potencjalnie możliwych sumach <T[i],target>,
# musimy iterować od tyłu, bo inaczej T[i] mogłoby zostać użyte kilka razy.

# Jeśli suma (sub_sum - T[i]) jest możliwa do uzyskania to suma (sub_sum), również jest możliwa.
