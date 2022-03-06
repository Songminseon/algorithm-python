import sys
from collections import deque

num = int(sys.stdin.readline())
queue_list = deque()


def push(num):
    queue_list.append(num)


def pop():
    if len(queue_list) == 0:
        print(-1)
    else:
        print(queue_list.popleft())


def front():
    if len(queue_list) == 0:
        print(-1)
    else:
        print(queue_list[0])


def back():
    if len(queue_list) == 0:
        print(-1)
    else:
        print(queue_list[len(queue_list) - 1])


def size():
    print(len(queue_list))


def empty():
    if len(queue_list) == 0:
        print(1)
    else:
        print(0)


for _ in range(num):
    command = sys.stdin.readline()
    category = command.split()[0]

    if category == "push":
        push(int(command.split()[1]))
    elif category == "pop":
        pop()
    elif category == "front":
        front()
    elif category == "back":
        back()
    elif category == "size":
        size()
    elif category == "empty":
        empty()
