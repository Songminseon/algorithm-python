def solution(word):
    answer = ""
    alpabet_str = "abcdefghijklmnopqrstuvwxyz"
    for i in alpabet_str:
        index = word.find(i)
        answer = answer + str(index) + " "
    return answer

word = input()

print(solution(word))
