a, b = map(int, input().split())
an1 = 1 if a >= b else 0
an2 = 1 if a > b else 0
an3 = 1 if a <= b else 0
an4 = 1 if a < b else 0
print(f"{an1}\n{an2}\n{an3}\n{an4}")