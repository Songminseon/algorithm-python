## 시간초과
# import sys

# num = int(sys.stdin.readline())
# num_list = []


# def shuffle():
#     num_list.append(num_list.pop(0))


# def drop():
#     num_list.pop(0)


# for i in range(num):
#     num_list.append(i + 1)


# while len(num_list) > 1:
#     drop()
#     shuffle()

# print(num_list[0])


# ## solution 1
# import sys

# num = int(sys.stdin.readline())
# num_list = []

# for i in range(num):
#     num_list.append(i + 1)


# while len(num_list) > 1:
#     if len(num_list) % 2:
#         t = [num_list[-1]]
#         t.extend(num_list[1::2])
#         num_list = t
#     else:
#         num_list = num_list[1::2]
# print(num_list[0])


import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for i in range(N):
    queue.append(i + 1)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())
