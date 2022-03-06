import sys
from collections import deque

N = int(sys.stdin.readline())  # 보드크기
K = int(sys.stdin.readline())  # 사과갯수

board = []

for _ in range(N):  # 보드판 깔기
    row = []
    for _ in range(N):
        row.append(0)
    board.append(row)

for _ in range(K):  # 사과 위치
    x, y = map(int, sys.stdin.readline().split())
    board[x - 1][y - 1] = 1

snake = deque([[1, 1]])  # 뱀의 경로, 몸길이를 고려해서 만약 새로운 지점을 가면 popleft랑 append실행
location = [1, 1]
time = 0
snake_direction = 1


def top():  # 상하좌우 움직임입니다. 고려해야할점은 좌표로 생각하면 안되고 행렬로 생각해야해요!
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

    # 현재 방향값을 기준으로 상하좌우 움직임 정의
    if snake_direction == 1:
        right()
    elif snake_direction == 2:
        bottom()
    elif snake_direction == 3:
        left()
    elif snake_direction == 4:
        top()

    # 게임이 끝나는 조건1 => 보드를 넘어가면 게임 끝
    if location[0] > N or location[0] < 1 or location[1] > N or location[1] < 1:
        break

    # 방향전환정보를 queue에 담아서 time이 방향전환에 걸리면 방향전환 실행
    if time in time_list:
        time_list.popleft()
        snake_direction = setDirection(direction_point.popleft(), snake_direction)

    # 움직임의 경우 2가지가 있습니다.
    # 1. 사과가 있는경우 꼬리는 그대로고 몸길이가 늘어나니 append만 실행
    # 2. 사과가 없으면 꼬리가 움직이니 pop실행 후 append

    if board[location[0] - 1][location[1] - 1] == 1:
        board[location[0] - 1][location[1] - 1] = 0
        snake.append([location[0], location[1]])
    else:
        # 게임이 끝나는 조건2 => 자기자신을 물어버리면 게임 끝, 뱀이 미음(ㅁ)자로 있다고 생각하면 됩니다.
        if location in snake:
            break
        snake.append([location[0], location[1]])
        snake.popleft()

print(time)
