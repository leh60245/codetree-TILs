a, b = map(int, input().split())
answer = 0
for i in range(a, b+1):
    if str(i).count('3') or str(i).count('6') or str(i).count('9'):
        answer += 1
        continue
    if i % 3 == 0:
        answer += 1
        continue
print(answer)