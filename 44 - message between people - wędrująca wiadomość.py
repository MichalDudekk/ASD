# 44 - message between people - wędrująca wiadomość
# Dana jest lista osób, które się znają (osoby reprezentowane jako liczby 0 do n-1). Pierwszego dnia
# osoba 0 przekazuje wiadomość wszystkim swoim znajomym. Drugiego dnia każdy znajomy przekazuje
# wiadomość swoim znajomym, którzy jej jeszcze nie znają, itd. Znajdź algorytm, który zwróci dzień,
# w którym najwięcej osób dowiedziało się wiadomości oraz liczbę osób, które otrzymały ją tego dnia.

from collections import deque

def message(G,s):
    days = [0]

    n = len(G)
    visited = [False]*n
    q = deque()

    visited[s] = True
    q.append( (s,0) )
    while q:
        v,time = q.popleft()

        if len(days) < time + 2:
            days.append(0)

        for u in G[v]:
            if visited[u]:
                continue
            visited[u] = True
            q.append( (u,time+1) )
            days[time+1] += 1

    candidate = 0
    res = 0
    for i in range(len(days)):
        if res < days[i]:
            res = days[i]
            candidate = i
    return candidate

# Przykładowy test - oczekiwana wartość: 3
G = [[1, 2], [0, 3, 4], [0, 5, 6], [1, 10], [1, 5, 7, 8, 7, 9, 11],
         [2, 4, 6], [2, 5], [4], [4], [4], [3], [4]]
print(message(G, 0))