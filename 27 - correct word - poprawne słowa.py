# 27 - correct word - poprawne słowa
# Dana jest funkcja dict(word) działająca w czasie O(1), która sprawdza, czy słowo należy do języka.
# Na wejściu otrzymujemy ciąg znaków bez spacji. Znajdź algorytm, który sprawdzi, czy możliwe jest
# wstawienie spacji w taki sposób, aby otrzymane słowa należały do zadanego języka.
# Przykład: "alamakotainiemapsa" można podzielić na "ala ma kota i nie ma psa".
# Algorytm powinien być szybki, ale najważniejsze jest, aby był poprawny.

# absolutnie przykładowa funkcja dict
def dict(word):
    words = ['ala', 'ma', 'kota', 'i', 'nie', 'ma', 'psa']
    if word in words:
        return True
    return False

def correct_word(s):
    n = len(s)

    F = [False for k in range(n)]
    # F[k] - czy można podzielić słowo s[0:k+1]

    for k in range(n):
        if dict(s[:k+1]):
            F[k] = True
        for i in range(k):
            if F[i] and dict(s[i+1:k+1]):
                F[k] = True
    return F[n-1]

# Przykładowy test - oczekiwana wartość: True
s = "alamakotainiemapsa"
print(correct_word(s))
# Przykładowy test - oczekiwana wartość: False
s = "alamakotainiemapsax"
print(correct_word(s))
