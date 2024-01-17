n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
answer = sum([i for i in arr if i % 2 != 0 and i % 3 == 0])
print(answer)