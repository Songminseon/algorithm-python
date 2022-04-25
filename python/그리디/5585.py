import sys

n = int(sys.stdin.readline())
rest = 1000 - n

count = 0
coin_list = [500, 100, 50, 10, 5, 1]

while rest != 0:
    for i in coin_list:
        if i <= rest:
            rest = rest - i
            count = count + 1
            break

print(count)
