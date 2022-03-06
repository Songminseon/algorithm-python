# import sys

# total_kg = int(sys.stdin.readline())
# count = total_kg
# n_3 = 0
# n_5 = 0


# while count > 2:
#     count -= 1
#     for i in range(total_kg, -1, -1):  # 5kg부터
#         for j in range(total_kg, -1, -1):  # 그다음 3kg
#             if i * 5 + j * 3 == total_kg:
#                 n_3 = j
#                 n_5 = i
#                 break

# total = n_3 + n_5

# if total == 0:
#     print(-1)
# else:
#     print(total)


# while else라는게 있구나... 처음 알았음

import sys

n = int(sys.stdin.readline())  # 설탕

result = 0  # 봉지 수

while n >= 0:
    if n % 5 == 0:  # 5로 나눈 나머지가 0인 경우
        result += n // 5  # 5로 나눈 몫 추력
        print(result)
        break
    n -= 3  # 설탕이 5의 배수가 될때까지 반복
    result += 1  # 봉지 추가

else:
    print(-1)  # while문이 거짓이 되면 -1 출력
