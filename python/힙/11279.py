import sys
import heapq

num = int(sys.stdin.readline())
myheap = []

for _ in range(num):
    number = int(sys.stdin.readline()) * -1
    if number == 0:
        if len(myheap) == 0:
            print(0)
        else:
            print(heapq.heappop(myheap) * -1)
    else:
        heapq.heappush(myheap, number)
