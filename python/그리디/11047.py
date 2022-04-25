import sys

n, k = map(int, sys.stdin.readline().split())
coin_list = []

count = 0

for _ in range(n):
    coin_list.append(int(sys.stdin.readline()))

while k != 0:
    for i in range(0, n):
        current_coin = coin_list[-(i + 1)]
        if current_coin <= k:
            count += 1
            k = k - current_coin
            break

print(count)
