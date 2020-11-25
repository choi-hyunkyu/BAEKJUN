# 백준 2739번 문제

N = int(input())

def calculate(N):
    for i in range(1, 10):
        print(N, "*", i, "=", N * i)

calculate(N)