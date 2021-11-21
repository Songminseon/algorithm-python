# import sys
# import heapq

# num = int(sys.stdin.readline())
# plusheap = []
# minusheap = []

# for _ in range(num):
#     number = int(sys.stdin.readline())

#     if number == 0:
#         if len(plusheap) + len(minusheap) == 0:
#             print(0)
#         elif len(plusheap) == 0:
#             print(heapq.heappop(minusheap) * -1)
#         elif len(minusheap) == 0:
#             print(heapq.heappop(plusheap))
#         else:
#             if plusheap[0] < minusheap[0]:
#                 print(heapq.heappop(plusheap))
#             else:
#                 print(heapq.heappop(minusheap) * -1)

#     elif number > 0:
#         heapq.heappush(plusheap, number)
#     elif number < 0:
#         heapq.heappush(minusheap, number * -1)

