# import sys
# from collections import deque

# num = int(sys.stdin.readline())

# for _ in range(num):
#     n, target = map(int, input().split())
#     priority = deque(map(int, input().split()))
#     index = deque()
#     count = 0

#     for i in range(n):
#         index.append(i)

#     while True:
#         if priority[0] == max(priority):  # 만약 우선순위가 최상위 우선순위가 맞다면
#             count += 1
#             if index[0] == target:
#                 break
#             priority.popleft()
#             index.popleft()
#         else:  # 아니면 뒤로 넘겻!
#             priority.append(priority.popleft())
#             index.append(index.popleft())
#     print(count)

from collections import deque


def sockMerchant(n, ar):
    ar.sort()
    my_queue = deque(ar)
    count = 0

    while True:
        if len(my_queue) <= 1:
            break
        else:
            value = my_queue.popleft()
            if value == my_queue[0]:
                count += 1
                my_queue.popleft()

    return count


print(sockMerchant(9, [42] * 100))
