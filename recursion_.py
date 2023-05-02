import sys


def recursion(n):
    if n < 5:
        print(n)
        recursion(n+1)


recursion(1)
# 1
# 2
# 3
# 4


def recursion(n):
    if n <= 0:
        return 0
    return n + recursion(n-1)


print(recursion(4))
# 10


# 최대 재귀 깊이 : 재귀 함수를 최대로 호출할 수 있는 횟수 파악
print(sys.getrecursionlimit())
# 1000
