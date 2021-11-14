import sys
import heapq

num = int(sys.stdin.readline())
myheap = []

for _ in range(num):
    number = int(sys.stdin.readline())
    if number == 0:
        if len(myheap) == 0:
            print(0)
        else:
            print(heapq.heappop(myheap))
    else:
        heapq.heappush(myheap, number)

print(myheap)
