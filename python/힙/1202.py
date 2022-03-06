import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
jewel_list = []
bag_list = []
total = 0

for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(jewel_list, [m, v])

for _ in range(k):
    c = int(sys.stdin.readline())
    heapq.heappush(bag_list, c)


capable_jewel = []

for _ in range(k):
    current_weight = heapq.heappop(bag_list)

    while jewel_list and current_weight >= jewel_list[0][0]:
        [weight, value] = heapq.heappop(jewel_list)  # 계속 다 담아, 가방에 담을 수 있는것은
        heapq.heappush(capable_jewel, -value)

    if capable_jewel:  # 담을 수 있는 것중에 가장 큰 값을 담은 힙
        total -= heapq.heappop(capable_jewel)
    elif not jewel_list:
        break

print(total)
