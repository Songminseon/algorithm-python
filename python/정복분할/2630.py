import sys

n = int(sys.stdin.readline())
graph = [list(map(int, input().split())) for _ in range(n)]

count_blue = 0
count_white = 0


def dfs(x, y, n):
    global count_blue, count_white
    value = graph[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != value:
                dfs(x, y, n // 2)
                dfs(x, y + n // 2, n // 2)
                dfs(x + n // 2, y, n // 2)
                dfs(x + n // 2, y + n // 2, n // 2)
                return

    if value == 1:
        count_blue += 1
    else:
        count_white += 1


dfs(0, 0, n)

print(count_white)
print(count_blue)

