# egzamin 2021 termin 2 zadanie 1 - intuse

from zad1testy import runtests

def intuse( I, x, y ):
    n = len(I)
    T = []

    for i in range(n):
        a,b = I[i]
        if a < x or a > y or b > y:
            continue
        T.append( (a,b,i) )
    T.sort()

    ends = {}
    ends[x] = None

    for a, b, i in T:
        if a not in ends.keys():
            continue
        if b not in ends.keys():
            ends[b] = []
        ends[b].append( (i,a) )

    cool_ends = {}
    res = {}
    def make_cool(v):
        if v in cool_ends.keys():
            return
        if ends[v] is None:
            return
        for i,a in ends[v]:
            res[i] = True
            make_cool(a)

    if y not in ends.keys():
        return []
    make_cool(y)

    ans = []
    for i in res.keys():
        ans.append(i)
    return ans

runtests( intuse )



