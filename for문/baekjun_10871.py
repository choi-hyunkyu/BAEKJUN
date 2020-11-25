# 백준 10871번 문제

N, X = map(int, input().split(' '))
A = list(map(int, input().split(' ')))

def classification(X, A):
    for index in range(N):
        if X > A[index]:
            print(A[index], end = ' ')

classification(X, A)