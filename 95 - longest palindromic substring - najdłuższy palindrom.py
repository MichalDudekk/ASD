# 95 - longest palindromic substring - najdłuższy palindrom
# Dany jest ciąg znaków. Znajdź najdłuższy podciąg, który jest palindromem.
# Opis algorytmu na dole

def longest_palindrome(s):
    n = len(s)
    longest = 1

    def palindrome(s,left,right,ctr):
        while left >= 0 and right < n and s[left] == s[right]:
            left-=1
            right+=1
            ctr += 2
        return ctr

    for k in range(n):
        ans = max(
            palindrome(s,k-1,k+1,1),    # k jest środkiem palindromu - palindrom nieparzystej długości np. 'ada'
            palindrome(s,k,k+1,0),      # k jest lewą literą środka - palindrom parzystej długości     np. 'abba'
            palindrome(s,k-1,k,0)       # k jest prawą literą środka - palindrom parzystej długości    np. 'abba'
        )
        longest = max(longest,ans)

    return longest

# Przykładowy test - oczekiwana wartość: 9
s = "abacabacabb"
print(longest_palindrome(s))

# Opis algorytmu - longest_palindrome(s) - O(n^2)
# Dla każdego znaku w ciągu traktuje go jako środek potencjalnego palindromu.
# Rozszerza się w lewo i prawo, sprawdzając, czy znaki są takie same (dla palindromów nieparzystych i parzystych).