import sys

num = int(sys.stdin.readline())
num_dummy = sys.stdin.readline()
sum = 0

for i in range(num):
    el = num_dummy[i]
    sum += int(el)

print(sum)    

