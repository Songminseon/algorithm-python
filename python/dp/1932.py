import sys

n = int(sys.stdin.readline())
num_list = []


for _ in range(n):
    num_list.append(list(map(int, sys.stdin.readline().split())))

k = 2

for i in range(1, n):
    for j in range(k):
        if j == 0:
            num_list[i][j] = num_list[i][j] + num_list[i - 1][j]
        elif i == j:
            num_list[i][j] = num_list[i][j] + num_list[i - 1][j - 1]
        else:
            num_list[i][j] = (
                max(num_list[i - 1][j - 1], num_list[i - 1][j]) + num_list[i][j]
            )
    k += 1

print(max(num_list[n - 1]))

# linear방식이 아니었네... 아 헷갈 계속 쌓아서 내려오는구나