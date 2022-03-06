import sys

sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.readline().split())

graph = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
count = 0


def dfs(i):
    visit[i] = 1
    for k in range(1, n + 1):
        if graph[i][k] == 1 and visit[k] == 0:
            dfs(k)


for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1


# 분리된 노드의 갯수를 파악하는거니 2606번문제랑 로직은 비슷한데
# if문 들어가는게 다름, 2606번 문제는 시작점으로부터 연결된 자식 노드의 갯수를 구하는거였음

for i in range(1, n + 1):
    if visit[i] == 0:
        dfs(i)
        count += 1

print(count)
