A_math, A_en = map(int, input().split())
B_math, B_en = map(int, input().split())
answer = 1 if A_math > B_math and A_en > B_en else 0
print(answer)