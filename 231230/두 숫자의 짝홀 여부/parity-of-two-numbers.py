a, b = map(int, input().split())
answer1 = "even" if a % 2 == 0 else "odd"
answer2 = "even" if b % 2 == 0 else "odd"
print(f"{answer1}\n{answer2}")