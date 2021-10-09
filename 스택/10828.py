import sys

def push(stack_list, value):
    stack_list.append(value)


def pop(stack_list):


    if(len(stack_list)==0):
        print(-1)
    else:
        print(stack_list.pop())
    

def size(stack_list):
    answer = len(stack_list)
    return answer

def empty(stack_list):
    answer = 0
    if(len(stack_list) == 0):
        answer = 1
    else:
        answer = 0
    return answer

def top(stack_list):
    answer = 0

    if(len(stack_list)==0):
        answer = -1
    else:
        answer = stack_list[len(stack_list)-1]
    return answer

num = int(sys.stdin.readline())

stack_list = []
command_list = []

for _ in range(num):
    command_list.append(sys.stdin.readline())

for i in command_list:

    category = i.split()[0]

    if category == "push":
       push(stack_list, int(i.split()[1]))

    elif category == "pop":
        pop(stack_list)

    elif category == "size":
        print(size(stack_list))

    elif category == "empty":
        print(empty(stack_list))

    elif category == "top":
        print(top(stack_list))

