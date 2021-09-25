# 펠린드롬수 문제

import sys

def solution(number):
    answer = "yes"
    str_num = str(number)
    for i in range(0, int(len(str_num)/2)):
        if (str_num[i] != str_num[len(str_num)-i-1]):
            answer = "no"
            break; 
    
    return answer


input_list = []

while(True):
    num = sys.stdin.readline().strip()
    if(num == "0"):
        break
    else:
        input_list.append(num)

for i in input_list:
    print(solution(i))