# 백준 11021번 문제

data = [list(map(int, input().split(' '))) for _ in range(int(input()))]

def sum_print(data):
    for i, sample in enumerate(data):
        A = sample[0]
        B = sample[1]
        C = A + B
        print("Case #{}: {}".format(i + 1, C))
        
sum_print(data)