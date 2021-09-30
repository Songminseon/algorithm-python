# def solution(num_list): // 내장함수
#     num_list.sort()
    
#     for i in num_list:
#         print(i)


def solution2(num_list): # bubble sort

    for i in range(0, len(num_list)):
        for j in range(0, len(num_list)-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    for i in num_list:
        print(i)


num = int(input())
num_list = []

for _ in range(num):
    num_list.append(int(input()))

solution2(num_list)