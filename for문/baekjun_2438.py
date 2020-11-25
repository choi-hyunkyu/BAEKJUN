# 백준 2438번 문제

N = int(input())

def drawstar(N):
    star = '*'
    for i in range(N):
        print(star * (i + 1))

drawstar(N)