import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
add, minus, multiple, divide = map(int, sys.stdin.readline().split())

max_value = -1e9
min_value = 1e9


def dfs(i, arr):
    global max_value, min_value, add, minus, multiple, divide

    if i == n:
        max_value = max(max_value, arr)
        min_value = min(min_value, arr)

    else:
        if add > 0:
            add -= 1
            dfs(i + 1, arr + num_list[i])
            add += 1
        if minus > 0:
            minus -= 1
            dfs(i + 1, arr - num_list[i])
            minus += 1
        if multiple > 0:
            multiple -= 1
            dfs(i + 1, arr * num_list[i])
            multiple += 1
        if divide > 0:
            divide -= 1
            dfs(i + 1, int(arr / num_list[i]))
            divide += 1


dfs(1, num_list[0])

print(max_value)
print(min_value)
