# import sys

# num = int(sys.stdin.readline())
# num_str = ""

# for _ in range(num):
#     num_str += str(input())

# for i in range(len(num_str)):
#     for j in range(len(num_str)-1):
#         if int(num_str[j]) > int(num_str[j+1]):
#             num_str = num_str.replace(num_str[j], "@").replace(num_str[j+1], num_str[j]).replace("@", num_str[j+1])
        
# for i in num_str:
#     print(i)

# 어려웠다. 처음에 간단한 문제로 생각했는데...
# 메모리가 제한되면 list사용 제한해야함 

import sys

num = int(sys.stdin.readline())

check_list = [0] * 10001

for i in range(num):
    prob_num = int(sys.stdin.readline())
    check_list[prob_num] += 1

for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)