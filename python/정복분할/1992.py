# import sys

# n = int(sys.stdin.readline())
# quard_tree = []

# for _ in range(n):
#     value = (sys.stdin.readline())
#     quard_tree.append(value)

# def transform(a,b,c,d):
#     sum = int(a) + int(b) + int(c) + int(d)
#     if sum == 0:
#         return 0
#     elif sum == 4:
#         return 1
#     else:
#         return "("+a+b+c+d+")"

# standard = n
# while standard == 2:

#     for i in range(0, standard/2, 2):
#         for j in range(0, standard/2, 2):
#             new_value = transform(quard_tree[i][j], quard_tree[i][j+1], quard_tree[i+1][j], quard_tree[i+1][j+1])

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]


def dnc(x, y, n):
    check = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != graph[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end="")
        n = n // 2
        dnc(x, y, n)  # 오른쪽 위
        dnc(x, y + n, n)  # 왼쪽 위
        dnc(x + n, y, n)  # 오른쪽 아래
        dnc(x + n, y + n, n)  # 왼쪽 아래
        print(")", end="")

    elif check == 1:
        print(1, end="")
    else:
        print(0, end="")


dnc(0, 0, n)
