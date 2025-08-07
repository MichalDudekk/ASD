# 13 - largest independent set - największy niezależny zbiór
# Dane jest drzewo binarne. Każdy węzeł w tym drzewie ma przypisaną wartość fun
# reprezentującą imprezowość dla danego pracownika na wydarzeniu. Znajdź maksymalną sumę imprezowości
# dla niezależnego zbioru węzłów. Zbiór węzłów jest niezależny jeśli żadne dwa węzły
# w tym zbiorze nie są połączone krawędzią (nie mogą być rodzicem i dzieckiem).
# Opis algorytmu na dole.

class Employee:
    def __init__(self, fun):
        self.fun = fun
        self.left = None
        self.right = None
        self.f = -1
        self.g = -1


def max_fun(root):

    def f(v):     # maksymalna suma imprezowości, kiedy v idzie na imprezę
        if v.f != -1:
            return v.f
        res = v.fun
        if v.left is not None:
            res += g(v.left)
        if v.right is not None:
            res += g(v.right)
        v.f = res
        return v.f

    def g(v):     # maksymalna suma imprezowości, kiedy v NIE idzie na imprezę
        if v.g != -1:
            return v.g
        res = 0
        if v.left is not None:
            res += max( f(v.left) , g(v.left) )
        if v.right is not None:
            res += max( f(v.right) , g(v.right) )
        v.g = res
        return v.g

    return max( f(root) , g(root) )

# Przykładowy test - oczekiwana wartość: 5
root = Employee(5)
root.left = Employee(1)
root.right = Employee(3)
print(max_fun(root))
# Przykładowy test - oczekiwana wartość: 260
root = Employee(10)
root.left = Employee(20)
root.right = Employee(30)
root.left.left = Employee(40)
root.left.right = Employee(50)
root.right.right = Employee(60)
root.left.right.left = Employee(70)
root.left.right.right = Employee(80)
print(max_fun(root))

# Opis algorytmu - max_fun(root) - O(n)
# f(v) - maksymalna suma imprezowości, kiedy v idzie na imprezę
# g(v) - maksymalna suma imprezowości, kiedy v NIE idzie na imprezę
# f(v) = v.fun + g(v.left) + g(v.right) - bo jeśli v idzie na impreze, to jego dzieci na pewno nie idą.
# g(v) = max( f(v.left) , g(v.left) ) + max( f(v.right) , g(v.right) ),
# bo jeśli v NIE idzie na impreze to jego dzieci mogą na nią pójść lub nie pójść.


