# 백준 2439번 문제

N = int(input())

def drawstar(N):
    star = '*'
    blank = ' '
    for i in range(1, N + 1):
        print(blank * (N - i) + star * i)

drawstar(N)