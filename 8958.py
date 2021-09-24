# OX 퀴즈

import sys

def solution(ox_list):
    for i in ox_list:
        total = 0
        accum = 0
        for j in i:
            if j == "O":
                accum += 1
                total += accum
            else:
                accum = 0
        print(total)
        

num = int(sys.stdin.readline())
ox_list = []

for i in range(0, num):
    ox_result = sys.stdin.readline()
    ox_list.append(ox_result)

solution(ox_list)

