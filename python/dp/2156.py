import sys

n = int(sys.stdin.readline())
num_list = [0] * 10000
dp = [0] * 10000

for i in range(n):
    num_list[i] = int(sys.stdin.readline())

dp[0] = num_list[0]
dp[1] = num_list[0] + num_list[1]
dp[2] = max(
    num_list[0] + num_list[2], num_list[1] + num_list[2], num_list[0] + num_list[1]
)

for i in range(3, n):
    dp[i] = max(
        dp[i - 2] + num_list[i],
        dp[i - 3] + num_list[i] + num_list[i - 1],
        dp[i - 1],
    )

print(max(dp))
