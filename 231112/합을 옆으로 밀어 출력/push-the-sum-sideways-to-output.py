n = int(input())
answer = 0
for _ in range(n):
    answer += int(input())
print(str(answer)[1:] + str(answer)[0])