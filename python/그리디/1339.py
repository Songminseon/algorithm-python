from re import A
import sys

n = int(sys.stdin.readline())
value_list = []
value_dict = {}

for _ in range(n):
    value = sys.stdin.readline()
    value_list.append(value.strip())

for i in range(n):
    value = value_list[i]
    value_length = len(value)
    for j in range(value_length):
        alpabet = value[j]
        digit = value_length - j - 1
        if alpabet not in value_dict:
            value_dict[alpabet] = 10**digit
        else:
            value_dict[alpabet] = value_dict[alpabet] + 10**digit

value_dict = sorted(value_dict.items(), key=lambda item: item[1], reverse=True)

sum = 0
start = 9

for _, j in value_dict:
    sum += start * j
    start -= 1

print(sum)
