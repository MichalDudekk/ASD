# 25 - sequence of strings - ciag napisów
# Dana jest sekwencja stringów (słów) S = [s[1], ..., s[n]] oraz string t. Wiadomo, że t można zapisać
# jako konkatenację (połączenie) pewnej liczby stringów z S (z powtórzeniami). Np. dla S = ['ab', 'abab', 'ba', 'bab', 'b'],
# string t = 'ababbab' można zapisać jako 'abab' + 'bab' (szerokość reprezentacji 3) lub
# 'ab' + 'ab' + 'ba' + 'b' (szerokość 1).
# Szerokość reprezentacji to długość najkrótszego stringa s[i] w tej reprezentacji.
# Algorytm ma znaleźć maksymalną możliwą szerokość reprezentacji t
# (czyli taką, gdzie najkrótszy string w reprezentacji jest najdłuższy).

def sequence(S,t):
    n = len(t)

    words = {}
    for word in S:
        words[word] = True

    F = [0 for _ in range(n)]
    # F[k] - maksymalna szerokość reprezentacji napisu t[0:k+1]

    for k in range(n):
        if t[:k+1] in words:
            F[k] = k+1
            continue
        for i in range(1,k):
            if F[i] != 0 and t[i+1:k+1] in words:
                F[k] = max(
                    F[k],
                    min( F[i] , k - i )
                )

    return F[n-1]

# Przykładowy test - oczekiwana wartość: 3
S = ['ab', 'abab', 'ba', 'bab', 'b']
t = 'ababbab'
print(sequence(S,t))
# Przykładowy test - oczekiwana wartość: 2
S = ['ab', 'ba', 'bab', 'b']
t = 'ababbab'
print(sequence(S,t))
# Przykładowy test - oczekiwana wartość: 4
S = ['a', 'aa', 'aaa', 'aaaa']
t = 'a'*16
print(sequence(S,t))
