# 백준 1330번 문제

a, b = map(int, input().split(' '))

def compare(a, b):
    if a > b:
        print(">")
    elif a < b:
        print("<")
    elif a == b:
        print("==")
    else:
        print("error")

compare(a, b)