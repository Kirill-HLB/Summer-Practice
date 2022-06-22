def factorial(n): # ф-я для нахождения n!
    f = 1
    while n > 1:
        f = f * n
        n -= 1
    return f


def countWithoutDouble(n, m): # ф-я для нахождения кол-ва сочетаний без повторений
    return factorial(n) / (factorial(m) * factorial(n - m))

def countWithDouble(n, k): # ф-я для нахождения кол-ва сочетаний с повторениями
    return factorial(n + k - 1) / (factorial(k) * factorial(n - (k - 1)))

def printWithout(m, n): # вывод сочетаний без повторений
    arr = []
    for i in range(m):
        arr.append(i)
    arr.append(n)
    arr.append(0)
    while True:
        print(arr[0:m])
        for j in range(len(arr)-1):
            if arr[j] + 1 == arr[j+1]:
                arr[j] = j
            else:
                break
        if j < m:
            arr[j] = arr[j] + 1
        else:
            break
    return arr

def printWith(m, k): # выводит сочетания с повторениями
    some = [0]*k
    while some is not None:
        yield some
        some = (generSome(some, m))
    return None


def generSome(some, m): # генерирует следующие сочетания на основании текущего
    k = len(some)
    for i in range(k - 1, -1, -1):
        if some[i] < m - 1:
            break
        else:
            return None
    some[i] = some[i] + 1
    for j in range(i+1, k):
        some[j] = some[i]
    return some

print("Введите 0, если хотите вывести сочетания без повторений")
print("Введите 1, если хотите вывести сочетания с повторениями")
check = int(input())
if check == 0:
    print("из скольки элементов?")
    n = int(input())
    print("по сколько?")
    m = int(input())
    print("Количество без повторений")
    printWithout(m, n)
    print(countWithoutDouble(n, m))
else:
    print("из скольки элементов?")
    m = int(input())
    print("по сколько?")
    k = int(input())
    print("Количество с повторениями")
    for s in printWith(m, k):
        print(s)
    print(countWithDouble(m, k))