start, end = map(int, input().split())
answer = 0
for i in range(start, end+1):
    if str(i) == str(i)[::-1]:
        answer += 1

print(answer)