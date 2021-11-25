import sys

n = int(sys.stdin.readline())
virus_num = int(sys.stdin.readline())

graph = []
visited = []

for _ in range(n + 1):
    graph.append([0] * (n + 1))
    visited.append(0)


for i in range(virus_num):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


def dfs(v):
    visited[v] = 1
    for i in range(1, n + 1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)


dfs(1)
count = 0

for i in range(2, n + 1):
    if visited[i] == 1:
        count += 1

print(count)
