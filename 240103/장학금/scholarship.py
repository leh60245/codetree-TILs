a, b = map(int, input().split())
answer  = 0 if a < 90 else 100000 if 95 <= b else 50000 if 90 <= b else 0
print(answer)