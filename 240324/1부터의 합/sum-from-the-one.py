n = int(input())
answer = 0
for i in range(1, 101):
    answer += i
    if answer >= n:
        print(i)
        break