import sys

n, m = map(int, sys.stdin.readline().split())

num_list = []


def dfs():
    if len(num_list) == m:
        print(" ".join(map(str, num_list)))
        return

    for i in range(1, n + 1):
        num_list.append(i)
        dfs()
        num_list.pop()


dfs()
