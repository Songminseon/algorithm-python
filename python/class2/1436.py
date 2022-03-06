import sys

def solution(user_input):
    number = 0
    count = 0
    while (True):
        number += 1
        if ("666" in str(number)):
            count += 1
        if (count == user_input):
            break

    return number

input = int(sys.stdin.readline())

print(solution(input))