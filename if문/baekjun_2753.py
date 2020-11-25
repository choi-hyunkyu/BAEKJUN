# 백준 2753번 문제

a = int(input())

def classification(a):
    if a % 400 == 0 or a % 4 == 0 and a % 100 != 0:
        print(1)
    else:
        print(0)

classification(a)