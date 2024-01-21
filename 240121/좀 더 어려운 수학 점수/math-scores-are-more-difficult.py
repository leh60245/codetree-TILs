a_math, a_en = map(int, input().split())
b_math, b_en = map(int, input().split())
answer = "A" if a_math > b_math else "B" if a_math < b_math else "A" if a_en > b_en else "B" 
print(answer)