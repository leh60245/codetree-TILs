i = int(input())
answer = 0
for n in range(1, i+1):
    answer += 1 if n % 400 == 0 else 0 if n % 100 == 0 else 1 if n % 4 == 0 else 0
    
print(answer)