# 85 - train timetable - rozkład pociągów
# Dany jest rozkład jazdy pociągów jako lista krotek (czas_przyjazdu, czas_odjazdu). Chcemy
# wiedzieć, czy nasza stacja, która ma n peronów, jest w stanie obsłużyć te pociągi bez
# kolizji (w danym momencie nie będzie "konkurencji pociągów" o dostępne perony).

def greedy_train_timetable(timetable, platform):
    timeline = []
    for start,end in timetable:
        timeline.append( (start,1) )
        timeline.append( (end,-1) )
    timeline.sort()
    current = 0
    for _ , kind in timeline:
        current += kind
        if current > platform:
            return False
    return True


# Przykładowy test - oczekiwana wartość: True
timetable = [(2, 4), (1, 5), (6, 7), (3, 5), (5, 8), (6, 8)]
platform = 3
print(greedy_train_timetable(timetable, platform))
# Przykładowy test - oczekiwana wartość: False
timetable = [(2, 4), (1, 5), (6, 7), (3, 5), (5, 8), (6, 8), (5, 7)]
platform = 3
print(greedy_train_timetable(timetable, platform))
# Przykładowy test - oczekiwana wartość: False
timetable = [(2, 4), (1, 5), (6, 7), (3, 5), (5, 8), (6, 8)]
platform = 2
print(greedy_train_timetable(timetable, platform))
