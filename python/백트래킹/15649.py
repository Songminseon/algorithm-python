n, m = map(int, input().split())

s = []


def f():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(1, n + 1):
        if i in s:
            continue
        s.append(i)
        print(s, "test", i, "i", "\n")
        f()
        s.pop()
        print("pop!, \n")


f()
