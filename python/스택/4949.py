import sys

def solution(text):
    answer = "yes"
    stack_list = []

    for i in text:
        if i == "(" or i == "[":
            stack_list.append(i)
        elif i == ")":
            if(len(stack_list) != 0 and stack_list[-1] == "("):
                stack_list.pop()
            else:
                answer = "no"
        elif i == "]":
            if(len(stack_list) != 0 and stack_list[-1] == "["):
                stack_list.pop()
            else:
                answer = "no"

    if (len(stack_list) != 0): #그냥 (( [[만 들어가는 경우 처리
        answer = "no"
    return answer

text_list = []

while True: 
    text = sys.stdin.readline().rstrip()

    if(text== "."):
        break
    else:
        text_list.append(text)

for i in text_list:
    print(solution(i))
