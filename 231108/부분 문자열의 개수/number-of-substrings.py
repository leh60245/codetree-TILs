A = input()
B = input()
answer = 0
for i in range(len(A)-len(B)+1):
    answer += 1 if B == A[i:i+len(B)] else 0
print(answer)