# import sys

# sys.setrecursionlimit(10**6)


# def append_star(LEN):
#     if LEN == 1:
#         return ["*"]
#     Stars = append_star(LEN // 3)
#     print(Stars, "stasrs")
#     L = []

#     for S in Stars:
#         L.append(S * 3)

#     for S in Stars:
#         L.append(S + " " * (LEN // 3) + S)

#     for S in Stars:
#         L.append(S * 3)

#     print(L, "l check")
#     return L


# n = int(sys.stdin.readline().strip())
# print("\n".join(append_star(n)))


def get_stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return matrix


star = ["***", "* *", "***"]
n = int(input())
e = 0
while n != 3:
    n = int(n / 3)
    e += 1

for i in range(e):
    star = get_stars(star)
for i in star:
    print(i)
