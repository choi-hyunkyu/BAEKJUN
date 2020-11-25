# 백준 2884번 문제

H, M = map(int, input().split(' '))

def early(H, M):
    if M >= 45:
        print(H, M - 45)
    elif H > 0 and M < 45:
        print(H - 1, M + 15)
    else:
        print(23, M + 15)

early(H, M)