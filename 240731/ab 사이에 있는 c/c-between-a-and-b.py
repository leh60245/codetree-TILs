a, b, c = map(int, input().split())
answer = "NO"
for i in range(a, b+1):
    if i % c == 0:
        answer = "YES"
        break
print(answer)