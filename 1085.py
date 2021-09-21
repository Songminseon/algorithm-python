# 간단한문제

def solution(x, y, w, h):
    answer = 0
    x_short = 0
    y_short = 0
    
    if (x < w-x):
        x_short = x
    else:
        x_short = w-x
    
    if (y < h-y):
        y_short = y
    else:
        y_short = h-y

    if (x_short < y_short):
        answer = x_short
    else:
        answer = y_short
    return answer

x,y,w,h = map(int, input().split())
print(solution(x,y,w,h))

