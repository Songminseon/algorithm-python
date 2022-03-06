# import sys

# num = int(sys.stdin.readline())
# sort_list = []

# for _ in range(num):
#     value = sys.stdin.readline().split()
#     sort_list.append([int(value[0]), int(value[1])])

# for i in range(num):
#     for j in range(num-1):
#         if sort_list[j][0] > sort_list[j+1][0]:
#             sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
#         elif sort_list[j][0] == sort_list[j+1][0]:
#             if sort_list[j][1] > sort_list[j+1][1]:
#                 sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]

# for i in sort_list:
#     answer = ""
#     for j in i:
#         answer += str(j) + " "
#     print(answer)

#시간 초과 뜸

import sys

num = int(sys.stdin.readline())
sort_list = []

for _ in range(num):
    value = sys.stdin.readline().split()
    sort_list.append([ int(value[0]), int(value[1])])

sort_list.sort()

for i in sort_list:
    answer = ""
    for j in i:
        answer += str(j) + " "
    print(answer)