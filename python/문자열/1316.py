def solution(word_list):
    answer = 0
    for i in word_list:
        count = 1
        current = i[0]
        parse_list = []
        for k in i:
            parse_list.append(k)
        char_list = list(set(parse_list))

        for k in range(0, len(i)):
            if(i[k] != current):
                count += 1
                current = i[k]
        if(count == len(char_list)):
            answer += 1
    return answer

number = int(input())
word_list = []

for _ in range(number):
    word_list.append(input())

print(solution(word_list))
