# 점화식을 잘 찾자

import sys

zero = [1, 0, 1]
one = [0, 1, 1]


def count(num):

    if len(zero) <= num:
        for i in range(len(zero), num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(str(zero[num]) + " " + str(one[num]))


num = int(sys.stdin.readline())

for _ in range(num):
    test_num = int(sys.stdin.readline())
    count(test_num)
