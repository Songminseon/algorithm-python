# 아 이분탐색!

import sys

prev_num = int(sys.stdin.readline())
prev_list = list(map(int, sys.stdin.readline().split()))
prev_list.sort()

new_num = int(sys.stdin.readline())
new_list = list(map(int, sys.stdin.readline().split()))

def binary(goal):
    left = 0
    right = prev_num - 1

    while left <= right:
        mid = (left+right) // 2
        if prev_list[mid] == goal:
            return True
        
        if goal  < prev_list[mid]:
            right = mid - 1
        else:
            left = mid+1

for i in range(new_num):
    if(binary(new_list[i])):
        print(1)
    else:
        print(0)