# 81 - activity selection - wybór zadań
# Dane jest n zadań z podanymi czasami rozpoczęcia i zakończenia (początek, koniec).
# Znajdź zbiór, który ma maksymalną liczbę niekolizyjnych zadań, które można wykonać
# w jednym przedziale czasowym.

def activity_selection(T):
    T.sort(key=lambda x:x[1])
    res = []
    prev = 0
    for start,end in T:
        if start < prev:
            continue
        prev = end
        res.append( (start,end) )
    return res

# Przykładowy test - oczekiwana wartość: [(1, 4), (5, 7), (8, 11), (12, 16)]
T = [(8, 12), (6, 10), (8, 11), (5, 7), (12, 16), (5, 9),
     (3, 5), (0, 6), (1, 4), (2, 14), (3, 9)]
print(activity_selection(T))