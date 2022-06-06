import sys

n = int(sys.stdin.readline())

def getMax(n):
    answer = ""
    if n%2 == 0:
        answer += "1"* (n//2)
    else:
        answer += "7"
        answer += "1" * ((n - 1) // 2 - 1)
    return answer

def getMin(n):
    ans = [0, 0, 1, 7, 4, 2, 6, 8, 10]
    a = ["1", "7", "4", "2", "0", "8"]
    
    for i in range(9, n+1):
        minList = []
        for j in range(2, 8):
            value = str(ans[i - j]) + a[j - 2]
            minList.append(int(value))
        ans.append(min(minList))
    return ans[n]


for _ in range(n):
    x = int(sys.stdin.readline())
    print(getMin(x), getMax(x))

