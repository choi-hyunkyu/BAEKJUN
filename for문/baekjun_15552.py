# 백준 15552번 문제

import sys

data = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(int(sys.stdin.readline()))]
        
def sum_print(data):
    for i, sample in enumerate(data):
        A = sample[0]
        B = sample[1]
        C = A + B
        print(C)
        
sum_print(data)