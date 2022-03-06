import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())

visit = [0] * (100000 + 1)


def bfs(start):
    
    dx = [1, -1, 0]

    q = deque()
    q.append(start)

    while q:
        x = q.popleft()
        if  x == k:
            return visit[x]
            
        for i in range(3):
            if dx[i] == 0:
                nx = x * 2
            else:
                nx = x + dx[i]
        
            if 0 <= nx <= 100000 and visit[nx] == 0:
                visit[nx] = visit[x] + 1
                q.append(nx)

print(bfs(n))