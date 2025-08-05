# 05 - coin change problem - problem wymiany monet
# Mamy daną tablicę wartości monet (np. [1, 2, 5]). Każdej monety możemy użyć
# nieskończenie wiele razy. Dla podanej kwoty (np. 5) należy znaleźć na ile różnych
# sposobów można wydać tę kwotę używając dostępnych monet.
# Uwaga: Kolejność monet nie ma znaczenia, tzn. 1+2+2 to to samo co 2+1+2.
# Opis algorytmu na dole.

# top down - rekurencyjnie z zapamiętywaniem na tablicy dwuwymiarowej - O(n * price)
def coin_change(T,price):
    n=len(T)
    F = [[-1 for k in range(price+1)] for w in range(n)]
    #F[w][k] = na ile sposobów mozna wydać liczbę k używając <0,w> wartości z tablicy T

    def recur(w,k):
        if w < 0 or k < 0:
            return 0
        if F[w][k] != -1:
            return F[w][k]
        if k==0:
            F[w][k] = 1
            return F[w][k]
        F[w][k] = recur( w , k - T[w] ) + recur( w-1 , k )
        return F[w][k]

    recur(n-1,price)
    return F[n-1][price]

# bottom up - eleganckie rozwiazanie iteracyjne, które zużywa mniej pamięci niż powyższe rozwiązanie rekurencyjne,
# złożoność obliczeniowa pozostaje jednak ta sama - O(n * price)
def coin_change_bottom_up(T,price):
    n = len(T)
    F = [0 for k in range( price+1 )]
    F[0] = 1
    # F[k] na ile sposobów mozna wydać liczbę k
    for i in range(n):
        for k in range( 1,price+1 ):
            if k - T[i] < 0:
                continue
            F[k] += F[ k - T[i] ]
    return F[price]


# Przykładowy test - oczekiwana wartość: 4
T = [1,2,5]
price = 5
print(coin_change(T,price))
print(coin_change_bottom_up(T,price))

# Przykładowy test - oczekiwana wartość: 7
T = [1, 2, 10]
price = 11
print(coin_change(T, price))
print(coin_change_bottom_up(T,price))

# Opis algorytmu - coin_change(T,price) - O(n * price)
# recur(w,k) - na ile sposobów mozna wydać liczbę k używając <0,w> wartości z tablicy T
# Warunkiem brzegowym rekurencji jest k==0, kwote 0 zawsze można wydac na dokładnie 1 sposób.
# recur(w,k) = recur( w , k - T[w] ) + recur( w-1 , k ),
# recur( w , k - T[w] ) - to próba wydawania liczby k za pomocą najwyższego nominału tak długo aż się da
# recur( w-1 , k ) - to próba wydawania liczby k za pomocą jednego nominału mniej
# Takie podejście zapewnia brak powtórzeń, bo w recur( w , k - T[w] ) zawsze użyjemy przynajmniej jednego nominału T[w],
# natomiast w recur( w-1 , k ) nigdy nie użyjemy nominału T[w]


