n = int(input())
for i in range(n,101):
    answer = "A" if i >= 90 else "B" if i >= 80 else "C" if i >= 70 else "D" if i >= 60 else "F"
    print(answer, end=" ")