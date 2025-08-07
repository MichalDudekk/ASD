# 10 - optimal strategy game pick - optymalna strategia gry
# Dana jest lista wartości. Gramy w grę przeciwko przeciwnikowi, gdzie każdy z nas
# wybiera jedną wartość z lewej lub prawej strony listy. Przeciwnik gra optymalnie.
# Jaka jest maksymalna wartość, jaką możemy zebrać, jeśli oboje gracze grają optymalnie.
# Opis algorytmu na dole.

# top down - O(n^2)
def strategy(T):
    n = len(T)
    F = [[-1 for k in range(n)] for w in range(n)]
    # F[w][k] = maksymalny zysk możliwy do uzyskania z przedziału <w,k> przy optymalnej grze przeciwnika

    P = [T[k] for k in range(n)]
    for k in range(1,n):
        P[k] += P[k-1]
    # P[i] - suma liczb z zakresu od T[0] do T[i], dzięki temu możemy uzyskać dostęp do sumy dowolnego przedziału
    # w czasie stałym O(1) - ( P[k] - P[w-1] ) = suma przedziału <w,k>

    def recur(w,k):
        if F[w][k] != -1:
            return F[w][k]
        if w==k:
            F[w][k] = T[w]
            return F[w][k]
        section = P[k]
        if w-1 >= 0:
            section -= P[w-1]
        # section - suma liczb z zakresu <w,k>
        right = section - recur(w,k-1)
        left = section - recur(w+1,k)
        F[w][k] = max(right,left)
        return F[w][k]

    recur(0,n-1)
    return F[0][n-1]

# Przykładowy test - oczekiwana wartość: 14
T = [3, 8, 4, 5, 1, 7, 6]
print(strategy(T))
# Przykładowy test - oczekiwana wartość: 11
T = [3, 9, 1, 2]
print(strategy(T))
# Przykładowy test - oczekiwana wartość: 2550
T = [i for i in range(1, 101)]
print(strategy(T))

# Opis algorytmu - strategy(T) - O(n^2)
# recur(w,k) = maksymalny zysk możliwy do uzyskania z przedziału <w,k> przy optymalnej grze przeciwnika
# P[i] - suma liczb z zakresu od T[0] do T[i]
# section - suma liczb z przedziału <w,k> uzyskiwana w czasie O(1) dzięki tablicy P
# recur(w,k) - oblicza maksymalny możliwy zysk biorąc maksimumum z dwóch wartości:
# left) - bierzemy wartość z lewej - otrzymujemy różnice sumy liczb z zakresu od T[w] do T[k] (czyli section) i recur(w+1,k),
#  czyli tego co może wziąc przeciwnik z przedziału <w+1,k> przy optymalnej grze
# right) - bierzemy wartość z prawej, resta analogicznie