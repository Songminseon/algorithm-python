import sys

n = int(sys.stdin.readline())
array_A = list(map(int, sys.stdin.readline().split()))
array_B = list(map(int, sys.stdin.readline().split()))

array_A.sort(reverse=True)
array_B.sort()

sum = 0

for i in range(n):
    sum += array_A[i] * array_B[i]

print(sum)
