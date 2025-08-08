# 17 - box stacking - układanie pudełek
# Dany jest zbiór trójwymiarowych pudełek, gdzie każde pudełko ma wysokość, szerokość i długość.
# Mamy nieograniczoną liczbę każdego rodzaju pudełek. Znajdź maksymalną wysokość układanki pudełek,
# gdzie każde pudełko na górze musi mieć ściśle mniejszą długość i szerokość niż pudełko pod spodem.
# Dodatkowo wypisz kolejność układania pudełek, aby osiągnąć tę maksymalną wysokość.
# UWAGA: pudełka można obracać.
# Opis algorytmu na dole.

def box_stacking(T):

    rotations = []  # musimy uwzględnić obroty pudełek
    for h,w,l in T:
        rotations.append( (h,w,l) )
        rotations.append( (h,l,w) )
        rotations.append( (l,h,w) )
        rotations.append( (l,w,h) )
        rotations.append( (w,l,h) )
        rotations.append( (w,h,l) )
    n = len(rotations)

    F = [-1 for _ in range(n)]
    # F[i] - maksymalna wysokość wieży z pudełek, którego podstawą jest i-te pudełko
    parent = [[ (rotations[i][0],rotations[i][1],rotations[i][2]) ] for i in range(n)]

    def recur(i):
        if F[i] != -1:
            return F[i]
        height = rotations[i][0]
        width = rotations[i][1]
        length = rotations[i][2]
        F[i] = height
        for j in range(n):
            if width > rotations[j][1] and length > rotations[j][2]:
                if F[i] < recur(j) + height:
                    F[i] = F[j] + height
                    parent[i] = parent[j] + [ (height,width,length) ]
        return F[i]

    ans = 0
    candidate = None
    for i in range(n):
        if recur(i) > ans:
            ans = F[i]
            candidate = i
    if candidate is not None:
        for box in parent[candidate]:
            print(box)
    return ans

# Przykładowy test - oczekiwana wartość: 23
boxes = [(1, 2, 4), (3, 2, 5), (3, 4, 9), (3, 2, 7)]
# (wysokość, szerokość, długość)
print(box_stacking(boxes))
# Przykładowy test - oczekiwana wartość: 10
boxes = [(5, 5, 5), (4, 4, 4), (1, 1, 1)]
print(box_stacking(boxes))

# Opis algorytmu - box_stacking(T) - O(n^2)
# F[i] - maksymalna wysokość wieży z pudełek, którego podstawą jest i-te pudełko
# Algorytm znajduje maksymalną wysokość wieży z pudełek 3D poprzez generowanie
# wszystkich możliwych obrotów pudełek a następnie rekurencyjne sprawdzanie
# wszystkich kombinacji z memoizacją (F[i]).
# Śledzenie sekwencji pudełek obsługuje tablica parent[i].