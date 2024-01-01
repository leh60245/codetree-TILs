a = float(input())
b = float(input())
answer = "High" if a >= 1 and b >= 1 else "Middle" if a >= 0.5 and b >= 0.5 else "Low"
print(answer)