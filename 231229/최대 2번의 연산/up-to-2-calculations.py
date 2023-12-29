a = int(input())
a = a // 2 if a % 2 == 0 else a
answer = (a+1) // 2 if a % 2 != 0 else a
print(answer)