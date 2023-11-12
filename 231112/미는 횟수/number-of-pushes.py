a = input()
b = input()
answer = 0
for i in range(len(b)):
    if a == b:
        break
    a = a[-1] + a[:-1]
    answer += 1
answer = -1 if answer == len(b) else answer
print(answer)