a, b = map(int, input().split())
answer1 = 1 if a < b else 0
answer2 = 1 if a == b else 0
print(f"{answer1} {answer2}")