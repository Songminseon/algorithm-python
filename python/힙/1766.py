# 위상정렬 공부합시다.

import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

num_list = [[] for i in range(n + 1)]
indegree = [0 for i in range(n + 1)]
myheap = []
result = []
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    num_list[x].append(y)
    indegree[y] += 1


for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(myheap, i)

while myheap:
    value = heapq.heappop(myheap)
    result.append(value)

    for i in num_list[value]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(myheap, i)

for i in result:
    print(i, end=" ")
