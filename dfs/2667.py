from collections import deque


def getScore(x):
    if x in ["a", "b"]:
        return 1
    elif x in ["c", "d", "e"]:
        return 2
    elif x in ["f", "g", "h"]:
        return 3
    elif x in ["i", "j", "k"]:
        return 4
    elif x in ["l", "m", "n"]:
        return 5
    elif x in ["o", "p", "q"]:
        return 6
    elif x in ["r", "s", "t"]:
        return 7
    elif x in ["u", "v", "w"]:
        return 8
    elif x in ["x", "y", "z"]:
        return 9


def countSubstrings(input_str):
    answer = 0
    comb_list = deque()

    for i in range(0, len(input_str)):  # 뽑기에서 시간초과, 메모리초과
        for j in range(0, len(input_str) - i):
            current = input_str[j : i + j + 1]
            comb_list.append(current)

    while comb_list:
        sum = 0
        v = comb_list.popleft()
        for i in v:
            sum += getScore(i)
        if sum % len(v) == 0:
            answer += 1

    return answer


print(countSubstrings("asdaskdjzzzzzzzzzzzzzzzzzz"))
