import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[0] * m for _ in range(n)]

for i in range(0, n):
    mirror = sys.stdin.readline()
    for j in range(0, m):
        if mirror[j] == "1":
            graph[i][j] = 1

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])
    
    return graph[n-1][m-1]

print(bfs(0,0))

