A = input()
command = input()
how_many = 0
for i in command:
    if i == "L":
        how_many += 1
    elif i == "R":
        how_many -= 1
    else:
        pass
how_many %= len(A)
answer = A[how_many:] + A[:how_many]
print(answer)