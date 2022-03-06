import sys

input = sys.stdin.readline

n, c = map(int, input().split())
house_list = []

for _ in range(n):
    house_list.append(int(input()))

house_list.sort()

start = 1
end = max(house_list) - 1

while start <= end:
    count = 1
    mid = (start + end) // 2
    loc = min(house_list) + mid

    for i in range (1, len(house_list)):
        if house_list[i] >= loc:
            count += 1
            loc = house_list[i] + mid

    if count >= c:
        start = mid + 1
    elif count < c:
        end = mid - 1


print(end)
