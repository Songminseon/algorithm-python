import sys

n, m = map(int, sys.stdin.readline().split())

num_list = []


def dfs():
    if len(num_list) == m:
        print(" ".join(map(str, num_list)))
        return

    for i in range(1, n + 1):
        if len(num_list) == 0 or num_list[-1] <= i:
            num_list.append(i)
            dfs()
            num_list.pop()


dfs()
