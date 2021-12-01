# import sys

# sys.setrecursionlimit(10000)

# num = int(sys.stdin.readline())


# def solution(num):
#     if num == 1:
#         return 1
#     elif num == 2:
#         return 2
#     else:
#         return solution(num - 1) + solution(num - 2)


# print(solution(num) % 10007)

import sys

s = [0, 1, 2]

for i in range(3, 1001):
    s.append(s[i - 2] + s[i - 1])

num = int(sys.stdin.readline())
print(s[num] % 10007)
