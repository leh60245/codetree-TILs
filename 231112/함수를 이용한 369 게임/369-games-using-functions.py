a, b = map(int, input().split())
arr = [3, 6, 9]
answer = 0
for i in range(a, b+1):
    if (i // 10 in arr) or (i % 10 in arr):
        answer += 1
        continue
    if i % 3 == 0:
        answer += 1
        continue
print(answer)