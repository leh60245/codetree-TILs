a, b = map(int, input().split())
answer = "0"
for i in range(a, b+1):
    if 1920 % i == 0 or 2880 % i == 0:
        answer = "1"
        break
print(answer)