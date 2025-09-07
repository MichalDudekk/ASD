# 90 - dishonest sellers - nieuczciwi sprzedawcy
# Igor dowiedział się o przecenach w sklepie i postanowił kupić n przedmiotów. Przeceny w sklepie
# potrwają tydzień, a Igor wie o każdym przedmiocie, że jego cena teraz to a[i], a po tygodniu
# przecen jego cena wyniesie b[i]. Nie wszyscy sprzedawcy są uczciwi, więc niektóre produkty
# mogą być teraz droższe niż po tygodniu przecen. Igor postanowił, że kupi co najmniej k
# przedmiotów teraz, ale z resztą poczeka tydzień, aby zaoszczędzić jak najwięcej pieniędzy.
# Twoim zadaniem jest określenie minimalnej kwoty, jaką Igor może wydać na zakup wszystkich
# n przedmiotów.

def dishonest_sellers(a,b,k):
    n = len(a)
    items = []
    for i in range(n):
        items.append( (a[i],b[i],b[i]-a[i]) )
    items.sort(reverse=True,key=lambda x:x[2])
    res = 0
    print(items)
    for i in range(n):
        if i >= k:
            if items[i][2] < 0:
                break
        res += items[i][0]
    for j in range(i,n):
        res += items[j][1]
    return res

# Przykładowy test - oczekiwana wartość: 243
a = [87, 96, 19, 81, 10, 88, 7, 49, 36, 21]
b = [11, 75, 28, 28, 74, 17, 64, 19, 81, 31]
k = 5
print(dishonest_sellers(a,b,k))