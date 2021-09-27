def solution(word):
    word_dict = {}
    answer = ""
    max = 0

    for i in str(word.upper()):
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1
    
    for i in word_dict:
        if (word_dict[i] > max):
            max = word_dict[i]
            answer = i
        elif word_dict[i] == max:
            answer = "?"
    print(answer)
    
    
word = input()
solution(word)
