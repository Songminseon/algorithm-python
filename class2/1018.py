# 접근법은 맞았는데 브루트포스를 몰라서 더 진전하지 못함

import sys

def solution(row, col, board_list):
    solution_list = []
    for i in range(0, row-7):
        for j in range(0, col-7):
            black_tile = 0
            white_tile = 0
            for k in range(i, i+8):
                for l in range(j, j+8):
                    if (k+l) % 2 == 0:
                        if board_list[k][l] != "W":
                            white_tile +=1
                        if board_list[k][l] != "B":
                            black_tile +=1
                    else:
                        if board_list[k][l] != "B":
                            white_tile +=1
                        if board_list[k][l] != "W":
                            black_tile +=1
            solution_list.append(white_tile)
            solution_list.append(black_tile)
    return min(solution_list)

row, col = map(int, input().split())
board_list = []

for i in range(row):
    row_detail = list(sys.stdin.readline().strip())
    board_list.append(row_detail)

print(solution(row, col, board_list))
