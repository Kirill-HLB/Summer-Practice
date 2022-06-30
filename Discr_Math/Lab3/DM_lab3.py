def gen(s, k):
    temp = s[0]
    for i in range(k):
        s[i] = s[i + 1]
    s[k] = temp


def prints(s):
    k = len(s) - 1
    n = k
    f = 1
    print(s)
    while k > 0:
        gen(s, k)
        if s[k] != k:
            print(s)
            k = n
        else:
            k = k - 1
    for i in range(1, len(s) + 1):
        f = f * i
    print(f)

s = [1, 2, 3, 4, 5]

prints(s)
