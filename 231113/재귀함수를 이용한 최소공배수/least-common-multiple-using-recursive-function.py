import sys
sys.setrecursionlimit(10**7)
n = int(input())
arr = list(map(int, input().split()))

# 최대 공약수 찾는 함수
def factor(num1, num2):
    remain = num1 % num2

    if remain == 0:
        return num2

    return factor(num2, remain)

# 최소 공배수 찾는 함수
def factor2(num1, num2):
    return num1 * num2 // factor(num1, num2)

# 순차적으로 최소
for i in range(n-1):
    arr[i+1] = factor2(arr[i], arr[i+1])

print(arr[-1])