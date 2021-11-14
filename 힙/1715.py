import sys
import heapq

num = int(sys.stdin.readline())
myheap = []

for _ in range(num):
    number = int(sys.stdin.readline())
    heapq.heappush(myheap, number)

count = len(myheap)
sum = 0

# for i in range(len(myheap)):

#     if count == 1:
#         sum += 0
#     else:
#         if i == 0:
#             value = heapq.heappop(myheap) * (count - 1)
#             sum += value
#         else:
#             value = heapq.heappop(myheap) * (count - i)
#             sum += value

for i in range(count - 1):
    if count == 1:
        sum += 0
    else:
        value_1 = heapq.heappop(myheap)
        value_2 = heapq.heappop(myheap)
        total = value_1 + value_2
        sum += total
        myheap.append(total)

print(sum)
