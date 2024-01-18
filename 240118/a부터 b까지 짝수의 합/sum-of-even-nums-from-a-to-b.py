a, b = map(int, input().split())
answer = sum([i for i in range(a, b+1) if i % 2 == 0])
print(answer)