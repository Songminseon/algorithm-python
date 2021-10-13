import sys

pip_line = sys.stdin.readline().strip()
pip_list = []
stack_list = []

for i in pip_line:
    pip_list.append(i)

sum = 0
for i in range(len(pip_list)):

    if pip_list[i] == "(":
        stack_list.append(i)
    else:
        if pip_list[i-1] == "(":
            stack_list.pop()
            sum += len(stack_list)
        else:
            stack_list.pop()
            sum +=1

print(sum)

# 빠르게 규칙을 찾아야했음
