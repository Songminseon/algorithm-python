import sys

t_num = int(sys.stdin.readline())

for _ in range(t_num):
    people_num = int(sys.stdin.readline())
    rank = []
    count = 1

    for _ in range(people_num):
        people_rank = list(map(int, sys.stdin.readline().split()))
        rank.append(people_rank)

    rank.sort()
    standard = rank[0][1]

    for i in range(people_num):
        second_rank = rank[i][1]

        # 자격o
        if standard > second_rank:
            count += 1
            standard = second_rank
        # 자격x

    print(count, "answer")
