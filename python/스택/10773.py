import sys

num = int(sys.stdin.readline())
stack_list = []
sum = 0

for _ in range(num):
    value = int(sys.stdin.readline())

    if value == 0:
        stack_list = stack_list[:-1]
    else:
        stack_list.append(value)

for i in stack_list:
    sum += i

print(sum)