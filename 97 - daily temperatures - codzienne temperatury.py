# 97 - daily temperatures - codzienne temperatury
# Dana jest tablica liczb całkowitych temperatures reprezentująca dzienne temperatury.
# Zwróć tablicę answer, taką że answer[i] jest liczbą dni, które musisz czekać po i-tym
# dniu, aby uzyskać cieplejszą temperaturę. Jeśli nie ma takiego dnia pozostaw answer[i] == 0.

def daily_temperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    monotonic_stack = []
    for i in range(n):
        while monotonic_stack and monotonic_stack[-1][0] < temperatures[i]:
            _, day = monotonic_stack.pop()
            answer[day] = i - day
        monotonic_stack.append((temperatures[i], i))
    return answer

# Przykładowy test - oczekiwana wartość: [1, 1, 4, 2, 1, 1, 0, 0]
temperatures = [73,74,75,71,69,72,76,73]
print(daily_temperatures(temperatures))
# Przykładowy test - oczekiwana wartość: [1, 1, 1, 0]
temperatures = [30,40,50,60]
print(daily_temperatures(temperatures))
# Przykładowy test - oczekiwana wartość: [2, 1, 0]
temperatures = [60,30,90]
print(daily_temperatures(temperatures))