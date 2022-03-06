# import sys

# num = int(sys.stdin.readline())

# count = 1
# num_list = [] # [4, 3, 6, 8, 7, 5, 2, 1]
# sequence_list = [] # [1,2,3,4,5,6,7,8]
# answer_list = []

# for i in range(num):
#     num_list.append(int(sys.stdin.readline()))
#     sequence_list.append(i+1)


# for i in range(len(sequence_list)):
#     value = sequence_list[i]
#     count += 1
    
#     if value == num_list[0]:
#         num_list = num_list[1:len(num_list)]
        
#         for i in range(count):
#             answer_list.append("+")

# import sys

# num = int(sys.stdin.readline())

# is_valid = True
# count = 1
# stack_list = []
# answer_list = []

# for i in range(num):
#     value = int(sys.stdin.readline())

#     while count <= num:
#         stack_list.append(count)
#         answer_list.append("+")
#         count += 1
    
#     if stack_list[-1] == value:
#         stack_list.pop()
#         answer_list.append("-")
#     else:
#         is_valid = False


# for i in answer_list:
#     print(i)


import sys

num = int(sys.stdin.readline())
stack_list = []
answer_list = []
count = 1
is_valid = True

for i in range(num):
    value = int(sys.stdin.readline())

    while count <= value:
        stack_list.append(count)
        answer_list.append("+")
        count += 1
    if stack_list[-1] == value:
        stack_list.pop()
        answer_list.append("-")
    else:
        is_valid = False

if is_valid:
    for i in answer_list:
        print(i)
else:
    print("NO")