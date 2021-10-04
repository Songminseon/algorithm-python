def solution(time_list):
    time_list.sort()
    sum = 0
    for i in range(len(time_list)):
        sum += time_list[i] * (len(time_list) - i)
        
    return sum

num = int(input())
time = input()
time_list = []

for i in time.split():
    time_list.append(int(i))

print(solution(time_list))