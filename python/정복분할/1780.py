import sys

n = int(sys.stdin.readline())
graph = [list(map(int, input().split())) for _ in range(n)]

count_minus = 0
count_zero = 0
count_plus = 0


def dfs(x, y, n):
    global count_minus, count_plus, count_zero

    value = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != value:
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * n // 3, y + l * n // 3, n // 3)
                return

    if value == -1:
        count_minus += 1
    elif value == 0:
        count_zero += 1
    elif value == 1:
        count_plus += 1


dfs(0, 0, n)

print(count_minus)
print(count_zero)
print(count_plus)
