# egzamin 2022 termin 1 zadanie 2 - widentall

from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

# O(n)
def wideentall( T ):

    count = [0]
    ctr = 0

    def dfs_visit(v,rank):
        v.x = rank
        nonlocal ctr
        while rank > ctr:
            count.append(0)
            ctr += 1
        count[rank] += 1

        if v.left is not None:
            dfs_visit(v.left,rank+1)
        if v.right is not None:
            dfs_visit(v.right,rank+1)

    def dfs_cut(v,best_rank):
        nonlocal ans
        if v.x == best_rank:
            if v.left is not None:
                ans += 1
            if v.right is not None:
                ans += 1
            return True

        l = False
        r = False

        if v.left is not None:
            l = dfs_cut(v.left, best_rank)
        if v.right is not None:
            r = dfs_cut(v.right, best_rank)

        if not l and not r:
            return False
        if l and not r:
            if v.right is not None:
                ans += 1
            return True
        if r and not l:
            if v.left is not None:
                ans +=1
            return True
        if l and r:
            return True

    dfs_visit(T,0)

    best_rank = 0
    res = count[0]
    for i in range(1,ctr+1):
        if res <= count[i]:
            res = count[i]
            best_rank = i

    ans = 0
    dfs_cut(T,best_rank)
    return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )

# Liczba zaliczonych testów: 10/10
# Liczba testów z przekroczonym czasem: 0/10
# Liczba testów z błędnym wynikiem: 0/10
# Liczba testów zakończonych wyjątkiem: 0/10
# Orientacyjny łączny czas : 0.50 sek.
# Status testów: A A A A A A A A A A