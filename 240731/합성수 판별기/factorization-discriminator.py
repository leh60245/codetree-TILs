a = int(input())
answer = "N"
for i in range(2, 501):
    if a % i == 0:
        answer = "C"
        break
print(answer)