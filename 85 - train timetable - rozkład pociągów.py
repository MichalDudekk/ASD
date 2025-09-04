# 85 - train timetable - rozkład pociągów
# Dany jest rozkład jazdy pociągów jako lista krotek (czas_przyjazdu, czas_odjazdu). Chcemy
# wiedzieć, czy nasza stacja, która ma n peronów, jest w stanie obsłużyć te pociągi bez
# kolizji (w danym momencie nie będzie "konkurencji pociągów" o dostępne perony).

def train_timetable(timetable, platform):
    points = {}
    for x,y in timetable:
        points[x] = True
        points[y] = True
    T = []
    for point in points.keys():
        T.append(point)
    T.sort()
    n = len(T)

    class Node:
        def __init__(self, value):
            self.val = value
            self.left = None
            self.right = None
            self.parent = None
            self.interval = ()
            self.ctr = 0

    def build_interval_tree(parent,a,b):
        mid = (abs(a - b)) // 2 + a
        new_node = Node(T[mid])
        new_node.parent = parent
        new_node.interval = (T[a],T[b])
        if a==b:
            return new_node
        if b == a+1:
            new_node.right = build_interval_tree(new_node,b,b)
            new_node.left = build_interval_tree(new_node,a,a)
            return new_node
        new_node.left = build_interval_tree(new_node,a,mid)
        new_node.right = build_interval_tree(new_node,mid,b)
        return new_node

    tree = build_interval_tree(None,0,n-1)

    def add_interval(vert,a,b):
        x,y = vert.interval
        if a == x and b == y:
            vert.ctr += 1
            return vert.ctr
        mid = vert.val

        res = 0
        if a < mid:
            res = max(res,add_interval(vert.left,a,mid))
        if b > mid:
            res = max(res,add_interval(vert.right,mid,b))
        return res + vert.ctr

    for a,b in timetable:
        res = add_interval(tree,a,b)
        if res > platform:
            return False
    return True

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
print(train_timetable(timetable, platform))
print(greedy_train_timetable(timetable, platform))
# Przykładowy test - oczekiwana wartość: False
timetable = [(2, 4), (1, 5), (6, 7), (3, 5), (5, 8), (6, 8), (5, 7)]
platform = 3
print(train_timetable(timetable, platform))
print(greedy_train_timetable(timetable, platform))
# Przykładowy test - oczekiwana wartość: False
timetable = [(2, 4), (1, 5), (6, 7), (3, 5), (5, 8), (6, 8)]
platform = 2
print(train_timetable(timetable, platform))
print(greedy_train_timetable(timetable, platform))