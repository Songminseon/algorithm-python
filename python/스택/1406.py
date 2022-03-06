# # 이게 왜 시간초과야...

# # import sys

# # text = sys.stdin.readline().rstrip()
# # num = int(sys.stdin.readline())
# # cursor = len(text)


# # for _ in range(num):
# #     command = sys.stdin.readline().rstrip()

# #     category = command.split()[0]

# #     if (category == "P"):
# #         value = command.split()[1]
# #         text = text[0:cursor] + value + text[cursor:len(text)]
# #         cursor += 1

# #     elif (category == "L"):
# #         if(cursor != 0 ):
# #             cursor -= 1
    
# #     elif (category == "D"):
# #         if (cursor != len(text)):
# #             cursor += 1

# #     elif (category == "B"):
# #         if (cursor != 0):
# #             text = text[0:cursor-1] + text[cursor:len(text)]         
# #             cursor -=1

# # print(text)

from sys import stdin

text_list = list(stdin.readline().strip())
stack_list = []

num = int(stdin.readline())

for _ in range(num):
    command = stdin.readline().rstrip()
    category = command.split()[0]

    if category == "P":
        text_list.append(command.split()[1])

    elif category == "L" and len(text_list) != 0:
        stack_list.append(text_list.pop())

    elif category == "D" and len(stack_list) != 0:
        text_list.append(stack_list.pop())

    elif category == "B" and len(text_list) != 0:
        text_list.pop()

print (''.join(text_list + list(reversed(stack_list))))