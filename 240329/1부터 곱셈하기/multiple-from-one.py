n = int(input())
answer = 1
for i in range(1, n+1):
    answer *= i
    if answer >= n:
        print(i)
        break