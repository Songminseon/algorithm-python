import sys

n = int(sys.stdin.readline())
house = []

for _ in range(n):
    n_house = list(map(int, sys.stdin.readline().split()))
    house.append(n_house)

for i in range(1, len(house)):
    house[i][0] = min(house[i - 1][1], house[i - 1][2]) + house[i][0]
    house[i][1] = min(house[i - 1][0], house[i - 1][2]) + house[i][1]
    house[i][2] = min(house[i - 1][0], house[i - 1][1]) + house[i][2]

print(min(house[n - 1][0], house[n - 1][1], house[n - 1][2]))

# 논리는 먼가 이해됐는데 그걸 로직으로 표현하기가 어려웠음
