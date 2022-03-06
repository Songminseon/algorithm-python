import sys

n, m = map(int, sys.stdin.readline().split())
tree_value = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(tree_value)

while start <= end:
    mid = (start + end) // 2
    sum = 0

    for i in tree_value:
        cut_height = i - mid

        if cut_height > 0:
            sum += cut_height

    if sum >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)


# while True:
#     answer = (start + end) // 2
#     sum = 0
#     for i in tree_value:
#         cut_height = i - answer
#         if cut_height > 0:
#             sum += cut_height

#     if sum > m:
#         start = answer
#     elif sum < m:
#         end = answer
#     else:
#         print(answer)
#         break
