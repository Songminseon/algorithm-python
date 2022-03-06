import sys
import heapq

left_heap = []
right_heap = []
num = int(sys.stdin.readline())

for _ in range(num):
    number = int(sys.stdin.readline())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -number)
    else:
        heapq.heappush(right_heap, number)

    if (
        len(left_heap) >= 1
        and len(right_heap) >= 1
        and left_heap[0] * -1 > right_heap[0]
    ):
        left_value = heapq.heappop(left_heap) * -1
        right_value = heapq.heappop(right_heap)

        heapq.heappush(left_heap, right_value * -1)
        heapq.heappush(right_heap, left_value)

    print(left_heap[0] * -1)


# 흠 어떻게[ 접근할지 잘 몰랐음

# 왼쪽 []  오른쪽 [] 이라는 가정하에 둘다 정렬이라는 상태라는 가정하에 왼쪽 오른쪽 끝값을 가져오면 됨
# 근데 그러면 시간복잡도가 올라가기 때문에 heap으로 접근해서 왼쪽에 루트값을 가져옴
