# 09 - number of binary strings - ilość łańcuchów binarnych
# Dla dodatniej liczby całkowitej n, oblicz liczbę różnych ciągów binarnych (0/1)
# długości n, w których nie występują dwa jedynki obok siebie (brak kolejnych '11').
# Opis algorytmu na dole.

# bottom up - O(n)
def binary_strings(n):
    F = [0 for k in range(n+1)]
    # F[i] - liczba wszystkich możliwych ciągów binarnych bez '11' długości i
    F[0] = 1 # ''
    F[1] = 2 # '0' , '1'

    for k in range(2,n+1):
        F[k] = F[k-1] + F[k-2]
    return F[n]

# ciekawostka - O(1)
def binary_strings_discrete(n):
    from math import sqrt
    ans = ( ( (5 + (3*sqrt(5)) ) / 10 ) * ( ( (1 + sqrt(5) ) / 2 )**n ) ) + ( ( (5 - (3*sqrt(5)) ) / 10 ) * ( ( (1 - sqrt(5) ) / 2 )**n ) )
    return round(ans)

# Przykładowy test - oczekiwana wartość: 8
n = 4
print(binary_strings(n))
# Przykładowy test - oczekiwana wartość: 377
n = 12
print(binary_strings(n))
# Przykładowy test - oczekiwana wartość: 6765
n = 18
print(binary_strings(n))

# Opis algorytmu - binary_strings(n) - O(n)
# F[i] - liczba wszystkich możliwych ciągów binarnych bez '11' długości i
# Dla każdego i możemy obliczyć wartość F[i] sumując:
# 1) F[i-1] - na końcu ciągu stawiamy '0'
# 2) F[i-2] - na końcu ciągu stawiamy '01'
# W ten sposób nigdy nie powstanie ciąg o dwóch jedynkach obok siebie.

# Ciekawostka - binary_strings_discrete(n) - O(1)
# Za pomocą znanej i LUBIANEJ matematyki dyskretnej można wyprowadzić nierekurencyjny wzór na n-ty wyraz ciągu,
# przez co algorytm ma złożoność O(1).