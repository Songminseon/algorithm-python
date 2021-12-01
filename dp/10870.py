import sys


def solution(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return solution(num - 2) + solution(num - 1)


number = int(sys.stdin.readline())
print(solution(number))
