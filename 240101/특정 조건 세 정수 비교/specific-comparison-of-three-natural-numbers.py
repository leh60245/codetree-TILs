a, b, c = map(int, input().split())
answer1 = 1 if a == min(a, b, c) else 0
answer2 = 1 if a == b and b == c else 0
print(f"{answer1} {answer2}")