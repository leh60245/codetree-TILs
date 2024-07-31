a = int(input())
answer = "N"
for i in range(2, a):
    if a % i == 0:
        answer = "C"
        break
print(answer)