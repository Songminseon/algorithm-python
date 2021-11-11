import sys

command = sys.stdin.readline()
n, k = map(int, command.split())

n_list = []
out_list = []
index = 0

for i in range(n):
    n_list.append(i + 1)


while len(n_list) > 0:
    index = (index + (k - 1)) % len(n_list)
    out_list.append(n_list.pop(index))

answer = "<"

for i in range(len(out_list) - 1):
    answer += str(out_list[i]) + ", "

answer += str(out_list[len(out_list) - 1]) + ">"

print(answer)

# 1 2 3 4 5 6 7
# 1 2 4 5 6 7     3
# 1 2 4 5 7       6
# 1 4 5 7         2
# 1 4 5           7
# 1 4             5
# 4               1
