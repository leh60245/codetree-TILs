y = int(input())
answer = "true" if y % 400 == 0 else "false" if y % 100 == 0 else "true" if y % 4 == 0 else "false"
print(answer)