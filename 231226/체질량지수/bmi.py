cm, kg = map(int, input().split())
bmi = int(kg // ((cm/100)**2))
print(bmi)
if bmi >= 25:
    print("Obesity")