from collections import deque
import sys

while True:
    length_list = list(map(int, sys.stdin.readline().split()))
    n = length_list.pop(0)

    if n == 0:
        break

    stack = deque()
    answer = 0

    for i in range(n):
        while len(stack) != 0 and length_list[stack[-1]] > length_list[i]:
            tmp = stack.pop()
            # print(stack, i, "stack")
            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1
            answer = max(answer, width * length_list[tmp])
        stack.append(i)
        # print(stack, i, "out")

    while len(stack) != 0:
        tmp = stack.pop()

        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1
        answer = max(answer, width * length_list[tmp])
    print(answer)
