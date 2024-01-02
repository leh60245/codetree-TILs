a, b, c = map(int, input().split())
answer = a if a <= b and a <= c else b if b <= c else c
print(answer)