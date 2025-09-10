# 94 - couples holding hands - pary trzymające się za ręce
# W rzędzie siedzi n par na 2n miejscach i chcą się trzymać za ręce.
# Ludzie i miejsca są reprezentowane przez tablicę liczb całkowitych row, gdzie row[i] to ID osoby
# siedzącej na i-tym miejscu. Pary są numerowane kolejno, pierwsza para to (0, 1), druga para to (2, 3)
# i tak dalej, aż do ostatniej pary (2n - 2, 2n - 1).
# Zwróć minimalną liczbę zamian, aby każda para siedziała obok siebie. Zamiana polega na wybraniu
# dowolnych dwóch osób, które wstają i zamieniają się miejscami.

def minSwapsCouples(row):
    idx = 0
    res = 0
    while idx < len(row):
        seek = row[idx] + 1
        if row[idx] % 2 == 1:
            seek -= 2
        i = idx + 1
        while row[i] != seek:
            i += 1
        if i != idx + 1:
            row[i], row[idx + 1] = row[idx + 1], row[i]
            res += 1
        idx += 2
    return res

# Przykładowy test - oczekiwana wartość: 1
row = [2,0,5,4,3,1]
print(minSwapsCouples(row))
# Przykładowy test - oczekiwana wartość: 1
row = [0,2,1,3]
print(minSwapsCouples(row))
# Przykładowy test - oczekiwana wartość: 0
row = [3,2,0,1]
print(minSwapsCouples(row))