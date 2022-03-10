import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if num_list[j] < num_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
