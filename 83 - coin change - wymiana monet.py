# 83 - coin change - wymiana monet
# Dana jest tablica liczb reprezentujących każdą monetę. Liczba monet, które posiadamy,
# jest nieskończona, więc nie musimy martwić się o to, ile monet mamy do dyspozycji.
# Następnie podana jest kwota i prosimy o znalezienie minimalnej liczby monet, które
# są potrzebne do uzyskania tej kwoty.
# Podejście zachłanne działa tylko jeżeli każdy nominał jest przynajmniej 2 razy większy od poprzedniego.

def coin_change(coins, amount):
    res = 0
    i = 0
    coins.sort(reverse=True)
    while amount > 0:
        if amount < coins[i]:
            i += 1
            if i == len(coins):
                return False
            continue
        amount -= coins[i]
        res += 1
    return res

# Przykładowy test - oczekiwana wartość: 6
amount = 237
coins = [1, 10, 100, 25, 5]
print(coin_change(coins, amount))
# Przykładowy test - oczekiwana wartość: False
amount = 238
coins = [2, 7, 100, 25, 5]
print(coin_change(coins, amount))

# Przykładowy test - oczekiwana wartość: 4 ***
amount = 8
coins = [1,4,5]
print(coin_change(coins, amount))
# *** - Tak jak zaznaczałem w poleceniu - podejście zachłanne działa tylko jeżeli każdy nominał jest
# przynajmniej 2 razy większy od poprzedniego. W tym przypadku coins to [1,4,5] a 5 nie jest 2 razy wieksze od 4,
# więc nasz algorytm zachłanny nie zadziała. Znajdzie on rozwiązanie 4 dla monet (5+1+1+1 = 8), jednak poprawne
# rozwiązanie to 2 dla monet (4+4 = 8). Jeśli dopuszczamy takie nominały to należy zastosować algorytm dynamiczny.
