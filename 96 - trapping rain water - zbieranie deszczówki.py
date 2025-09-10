# 96 - trapping rain water - zbieranie deszczówki
# Dane jest n nieujemnych liczb całkowitych reprezentujących mapę wysokości, gdzie szerokość każdego słupka
# wynosi 1. Oblicz, ile kratek wody zostanie uwięzionych po deszczu po deszczu.
# Np. dla tablicy [1,0,0,1] odpowiedź to 2 - dwie kratki wody zostaną uwięzione między polem 0 a polem 3.

def trap(height):
    res = 0
    max_left = 0
    max_right = 0
    left = 0
    right = len(height) - 1
    while left <= right:
        max_left = max(max_left, height[left])
        max_right = max(max_right, height[right])
        if height[left] < height[right]:
            res += min(max_left, max_right) - height[left]
            left += 1
            continue
        res += min(max_left, max_right) - height[right]
        right -= 1
    return res

# Przykładowy test - oczekiwana wartość: 2
height = [1,0,0,1]
print(trap(height))
# Przykładowy test - oczekiwana wartość: 0
height = [1,2,3,1]
print(trap(height))
# Przykładowy test - oczekiwana wartość: 6
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
# Przykładowy test - oczekiwana wartość: 9
height = [4,2,0,3,2,5]
print(trap(height))