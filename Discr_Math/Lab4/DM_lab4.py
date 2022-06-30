#Размещения без повторений
def swap(mas, i, j):
    mas[i], mas[j] = mas[j], mas[i]

def reverse(mas, index):
    sd = index + 1
    n = len(mas)
    for i in range((n - sd)// 2):
        mas[sd+i], mas[n-1-i] = mas[n-1-i], mas[sd+i]

def perestanovka(k, mas):
    n = len(mas)
    for j in range(k, n):
        if mas[j] > mas[k - 1]:
            break
    else:
        j = n
    if j < n:
        swap(mas, k - 1, j)
        return mas[:k:]
    else:
        reverse(mas, k - 1)
        for i in range(k - 2, -1, -1):
            if mas[i] < mas[i + 1]:
                break
        else:
            return None
        for j in range(n - 1, i, -1):
            if mas[j] > mas[i]:
                break
        swap(mas, i, j)
        reverse(mas, i)
        return mas[:k:]

#размещения с повторениями
def permutation(n, k):
    perm = [0 for i in range(k)]
    while True:
        print(perm)
        for i in range(k - 1, -1, -1):
            if perm[i]< n -1:
                break
        else:
            return
        perm[i]+= 1
        for j in range(i + 1, k):
            perm[j] =0

def fact(m):
    rz = 1
    while m > 1:
        rz *= m
        m -= 1
    return rz

def C(m, n):
    return fact(m)/fact(m - n)
def K(m, n):
    return m**n

print("Введите 0, если размещения без повторений, введите 1, если размещения с повторениями")
i = int(input())
if i == 0:
    mas = [0, 1, 2, 3, 4]
    k = 3
    perm = mas[:k:]
    n = len(mas)
    print("Количество размещений без повторений:")
    print(C(n, k))
    while perm is not None:
        print (perm)
        perm = perestanovka(k, mas)
else:
    print("Введите n:")
    n = int(input())
    print("Введите k:")
    k = int(input())
    print("Количество размещений с повторений:")
    print(K(n, k))
    permutation(n, k)
