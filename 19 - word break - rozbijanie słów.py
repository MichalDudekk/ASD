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

# bottom up ze słownikiem, z inaczej zdefiniowaną funkcją - O(n^2)
def word_break_best(words, s):
    n = len(s)
    words_dict = {}                     # Konwersja na słownik dla O(1) sprawdzeń
    for word in words: words_dict[word] = True
    F = [False for _ in range(n + 1)]   # F[i] = True jeśli s[0:i] da się podzielić
    F[0] = True                         # Pusty ciąg jest zawsze "podzielny"

    for i in range(1, n + 1):
        for j in range(i):
            if F[j] and s[j:i] in words_dict:
                F[i] = True
                break                   # Nie trzeba sprawdzać dalszych podziałów

    return F[n]

# Przykładowy test - oczekiwana wartość: True
words = ["self", "th", "is", "famous", "Word", "break", "b", "r", "e", "a",
         "k", "br", "bre", "break", "ak", "problem"]
s = "Wordbreakproblem"
print(word_break(words,s))
print(word_break_dict(words,s))
print(word_break_best(words,s))
# Przykładowy test - oczekiwana wartość: False
words = ["self", "th", "is", "famous", "Word", "break", "b", "r", "e", "a",
         "k", "br", "bre", "break", "ak", "problem"]
s = "Wordbrxakproblem"
print(word_break(words,s))
print(word_break_dict(words,s))
print(word_break_best(words,s))
# Przykładowy test - oczekiwana wartość: True
words = ["self", "th", "is", "famous", "Word", "break", "b", "r", "e", "a",
         "k", "br", "bre", "break", "ak", "problem","x"]
s = "Wordbrxakproblem"
print(word_break(words,s))
print(word_break_dict(words,s))
print(word_break_best(words,s))

# Opis algorytmu - word_break(words,s) - O(n^2 * (n + len(words)) )
# recur(w,k) - czy ciąg znaków s[w:k+1] można podzielić na sekwencję słów z listy words
# Algorytm dla każdego wywołania funkcji recur(w,k) sprawdza czy word (word = s[w:k+1]) znajduje się w tablicy
# words ( złożoność O(len(words)) ), jeśli się nie znajduje to sprawdza każdy możliwy podział na
# słowa word na dwa ( złożoność O(n) ). Jeśli oba z powstałych słów da się podzielić to słowo word również
# da się podzielić.
# Liczba unikalnych podproblemów: O(n^2)
# Rozwiązanie pojedyńczego podproblemu: O(n + len(words)) - przy użyciu słownika O(len(words)) redukuje się do O(1)

# Opis algorytmu - word_break_best(words,s) - O(n^2)
# F[i] - czy s[0:i] da się podzielić
# Algorytm dla każdego wywołania pętli dzieli słowo s[0:i] na dwa s[0:j] i s[j:i].
# To czy s[0:j] da się podzielić zostało już wcześniej obliczone i jest zapisane w F[j].
# Pozostaje sprawdzić czy s[j:i] jest słowem w words, korzystając ze słownika możemy to zrobić w czasie stałym O(1).
