g = int(input())
age = int(input())
answer = "MAN" if g == 0 and age >= 19 else "WOMAN" if g == 1 and age >= 19 else "BOY" if g == 0 else "GIRL"
print(answer)