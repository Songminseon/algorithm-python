# import sys

# def solution(line_list, goal):
#     answer = 1

#     while (True):
#         amount = 0
#         for i in line_list:
#             amount += i // answer 

#         if (amount >= goal):
#             answer +=1
#         else:
#             answer -=1
#             break
        
#     print(answer)
#     return answer


# k, goal_number = map(int, input().split())
# line_list = []

# for i in range(0, k):
#     line = int(sys.stdin.readline().strip())
#     line_list.append(line)

# print(solution(line_list, goal_number))

# 브루트 포스 실패 O(n^2)이라 실패

import sys

def solution(line_list, goal_number):
    start, end = 1, max(line_list)

    while start <= end:
        mid = (start + end) // 2
        lines = 0
        for i in line_list:
            lines += i // mid

        if lines >= goal_number:
            start = mid + 1
        else:
            end = mid - 1         
    return start
k, goal_number = map(int, input().split())
line_list = []

for i in range(0, k):
    line = int(sys.stdin.readline().strip())
    line_list.append(line)

print(solution(line_list, goal_number))