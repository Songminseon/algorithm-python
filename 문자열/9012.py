num = int(input())

def solution(prob):
    answer = ""
    prob_list = []
    stack_list = []

    for i in prob:
        prob_list.append(i)

    for i in prob_list:
        if i == "(":
            stack_list.append(i)
        else:
            if len(stack_list) > 0:
                stack_list.pop()
            else:
                stack_list.append(i)
                break 


    if len(stack_list) == 0:
        answer = "YES"
    else:
        answer = "NO"

    return answer

for i in range(num):
    prob = input()
    print(solution(prob))

