# 브루투 포스 문제
# break를 안걸고 풀이해야함, 나중에 remove활용

import sys

def solution(tall_list):
    tall_list.sort()
    
    sum = 0
    ban_one = 0
    ban_two = 0
    for i in tall_list:
        sum += i

    for i in range(0, len(tall_list)-1):
        for j in range(i+1,  len(tall_list)):
            check_sum = sum
            check_sum -= tall_list[i]
            check_sum -= tall_list[j]

            if check_sum == 100:
                ban_one = tall_list[i]
                ban_two = tall_list[j]

    tall_list.remove(ban_one)
    tall_list.remove(ban_two)

    for i in tall_list:
        print(i)

num = 9
tall_list = []

for _ in range(num):
    tall_list.append(int(sys.stdin.readline()))


solution(tall_list)
