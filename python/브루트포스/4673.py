total_num = [i for i in range(1, 10001)]
sum_num = []

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    sum_num.append(i)

self_num = sorted(set(total_num) - set(sum_num))


for i in self_num:
    print(i)
