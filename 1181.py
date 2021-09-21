# 1 try

# def solution(word_list):

#     for i in range(0, len(word_list)):
#         for j in range(i+1, len(word_list)):
#             if(len(word_list[i]) > len(word_list[j]) or  (len(word_list[i]) == len(word_list[j]) and word_list[i] > word_list[j])):
#                 word_list[j], word_list[i] = word_list[i], word_list[j]
                
#     return word_list

# number = int(input())
# user_list = []

# for i in range(0, number):
#     word = input()
#     user_list.append(word)

# new_list = solution(user_list)

# for i in range(0, len(new_list)-1):
#     if(new_list[i] != new_list[i+1]):
#         print(new_list[i])
# print(new_list[len(new_list)-1])

# 2 try

# 단어 정렬 문제
# 내장함수 잘 이용하자!
# input은 sys.stdin.readline() 사용

import sys

def solution(word_list):

    word_list = list(set(word_list))
    word_list.sort()
    word_list.sort(key=len)

    return word_list

number = int(sys.stdin.readline())
user_list = []

for i in range(0, number):
    word = sys.stdin.readline().strip()
    user_list.append(word)

my_list = solution(user_list)

for i in my_list:
    print(i)

