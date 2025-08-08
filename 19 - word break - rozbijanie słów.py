# 19 - word break - rozbijanie słów
# Dany jest ciąg znaków i lista słów. Sprawdź, czy ciąg można podzielić na sekwencję
# słów z listy oddzielonych spacjami (każdy element sekwencji musi występować w liście).
# Opis algorytmu na dole.

# top down - O(n^2 * (n + len(words)) )
def word_break(words,s):
    n = len(s)

    F = [[-1 for k in range(n)] for w in range(n)]
    # F[w][k] - czy ciąg znaków s[w:k+1] można podzielić na sekwencję słów z listy words
    # F[w][k] == 1 - ciąg da się podzielić
    # F[w][k] == 0 - ciąg nie da się podzielić
    # F[w][k] == -1 - wartość początkowa, znaczy że program jeszcze nie sprawdził czy ciąg da się podzielić

    def recur(w,k):
        if F[w][k] != -1:
            return F[w][k]
        word = s[w:k+1]
        if word in words:
            F[w][k] = 1
            return F[w][k]
        for i in range(w+1,k+1):
            if recur(w,i-1) == 1 and recur(i,k) == 1:
                F[w][k] = 1
                return F[w][k]
        F[w][k] = 0
        return F[w][k]

    return True if recur(0,n-1) == 1 else False

# top down ze słownikiem - O(n^3)
def word_break_dict(words,s):
    n = len(s)

    words_dict = {}
    for string in words:
        words_dict[string] = True

    F = [[-1 for k in range(n)] for w in range(n)]
    # F[w][k] - czy ciąg znaków s[w:k+1] można podzielić na sekwencję słów z listy words
    # F[w][k] == 1 - ciąg da się podzielić
    # F[w][k] == 0 - ciąg nie da się podzielić
    # F[w][k] == -1 - wartość początkowa, znaczy że program jeszcze nie sprawdził czy ciąg da się podzielić

    def recur(w,k):
        if F[w][k] != -1:
            return F[w][k]
        word = s[w:k+1]
        if word in words_dict:
            F[w][k] = 1
            return F[w][k]
        for i in range(w+1,k+1):
            if recur(w,i-1) == 1 and recur(i,k) == 1:
                F[w][k] = 1
                return F[w][k]
        F[w][k] = 0
        return F[w][k]

    return True if recur(0,n-1) == 1 else False

# Przykładowy test - oczekiwana wartość: True
words = ["self", "th", "is", "famous", "Word", "break", "b", "r", "e", "a",
         "k", "br", "bre", "break", "ak", "problem"]
s = "Wordbreakproblem"
print(word_break(words,s))
print(word_break_dict(words,s))
# Przykładowy test - oczekiwana wartość: False
words = ["self", "th", "is", "famous", "Word", "break", "b", "r", "e", "a",
         "k", "br", "bre", "break", "ak", "problem"]
s = "Wordbrxakproblem"
print(word_break(words,s))
print(word_break_dict(words,s))
# Przykładowy test - oczekiwana wartość: True
words = ["self", "th", "is", "famous", "Word", "break", "b", "r", "e", "a",
         "k", "br", "bre", "break", "ak", "problem","x"]
s = "Wordbrxakproblem"
print(word_break(words,s))
print(word_break_dict(words,s))

# Opis algorytmu - word_break(words,s) - O(n^2 * (n + len(words)) )
# recur(w,k) - czy ciąg znaków s[w:k+1] można podzielić na sekwencję słów z listy words
# Algorytm dla każdego wywołania funkcji recur(w,k) sprawdza czy word (word = s[w:k+1]) znajduje się w tablicy
# words ( złożoność O(len(words)) ), jeśli się nie znajduje to sprawdza każdy możliwy podział na
# słowa word na dwa ( złożoność O(n) ). Jeśli oba z powstałych słów da się podzielić to słowo word również
# da się podzielić.
# Liczba unikalnych podproblemów: O(n^2)
# Rozwiązanie pojedyńczego podproblemu: O(n + len(words)) - przy użyciu słownika O(len(words)) redukuje się do O(1)