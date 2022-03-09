import sys

n = int(sys.stdin.readline())

score = [0 for _ in range(301)]
dp = [0 for _ in range(301)]

for i in range(n):
    score[i] = int(sys.stdin.readline())

dp[1] = score[0]
dp[2] = score[0] + score[1]
dp[3] = max(score[0] + score[2], score[1] + score[2])

for i in range(4, n + 1):
    dp[i] = max(dp[i - 2] + score[i - 1], dp[i - 3] + score[i - 2] + score[i - 1])

print(dp[n])
