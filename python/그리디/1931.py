import sys

n = int(sys.stdin.readline())

time_table = []

for _ in range(n):
    input_value = list(map(int, sys.stdin.readline().split()))
    time_table.append(input_value)

time_table = sorted(time_table, key=lambda a: a[0])
time_table = sorted(time_table, key=lambda a: a[1])

count = 0
end = 0

for i, j in time_table:
    if i >= end:
        count += 1
        end = j

print(count)
