import sys

num =  int(sys.stdin.readline())

def solution(num):
    num_list = []
    answer = ""
    for i in str(num):
        num_list.append(int(i))
    
    num_list.sort(reverse=True)
    
    for i in num_list:
        answer += str(i)

    return answer
    
print(solution(num))