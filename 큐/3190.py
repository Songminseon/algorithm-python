import sys
from collections import deque

N = int(sys.stdin.readline())  # 보드크기
K = int(sys.stdin.readline())  # 사과갯수

board = []

for _ in range(N):
    row = []
    for _ in range(N):
        row.append(0)
    board.append(row)

for _ in range(K):  # 사과 위치
    x, y = map(int, sys.stdin.readline().split())
    board[x - 1][y - 1] = 1

snake = deque([[1, 1]])  # 뱀의 경로
location = [1, 1]
time = 0
snake_direction = 1


def top():
    location[0] = location[0] - 1


def bottom():
    location[0] = location[0] + 1


def left():
    location[1] = location[1] - 1


def right():
    location[1] = location[1] + 1


def setDirection(x, direction):
    my_direction = direction

    if x == "L":  # right => 0, 왼쪽 꺽으면 4
        my_direction -= 1
        if my_direction == 0:
            my_direction = 4

    else:
        my_direction += 1
        if my_direction == 5:
            my_direction = 1

    return my_direction


L = int(sys.stdin.readline())

time_list = deque()
direction_point = deque()

for _ in range(L):
    x, c = map(str, sys.stdin.readline().split())
    time_list.append(int(x))
    direction_point.append(c)


while True:
    time += 1

    if snake_direction == 1:
        right()
    elif snake_direction == 2:
        bottom()
    elif snake_direction == 3:
        left()
    elif snake_direction == 4:
        top()

    if location[0] > N or location[0] < 1 or location[1] > N or location[1] < 1:
        break

    if time in time_list:
        time_list.popleft()
        snake_direction = setDirection(direction_point.popleft(), snake_direction)

    if board[location[0] - 1][location[1] - 1] == 1:
        board[location[0] - 1][location[1] - 1] = 0
        snake.append([location[0], location[1]])
    else:
        if location in snake:
            break
        snake.append([location[0], location[1]])
        snake.popleft()

print(time)
