import sys

# 더하기 먼저

equation = sys.stdin.readline()
sum = 0

s = equation.split("-")

for i in s[0].split("+"):
    sum += int(i)

for i in s[1:]:
    for j in i.split("+"):
        sum -= int(j)

print(sum)
