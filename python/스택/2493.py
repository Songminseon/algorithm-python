# import sys

# num = int(sys.stdin.readline())

# top_list = list(map(int, sys.stdin.readline().split()))
# top_list = list(reversed(top_list))

# answer_list = []
# answer = ""

# for i in range(0, len(top_list)):
#     value = 0
#     for j in range(i, len(top_list)):
#         if (top_list[i] < top_list[j]):
#             value = j
#             break
#     answer_list.append(value)

# answer_list = list(reversed(answer_list))

# for i in answer_list:
#     if (i == 0):
#         answer += "0 "
#     else:
#         answer += str(num - i) + " "

# print(answer)

# 시간복잡도 해결 못함 ㅠㅠ

import sys

num = int(sys.stdin.readline())
top_list = list(map(int, sys.stdin.readline().split()))
stack_list = []
result = [0] * num

for i in range(num):
    current_top = top_list[i]

    while stack_list and top_list[stack_list[-1]] < current_top: # stack이 비거나 현재 탑이 더 작으면 멈춤
        stack_list.pop()
    if stack_list:
        result[i] = stack_list[-1] + 1

    stack_list.append(i)
print(' '.join(map(str, result)))
