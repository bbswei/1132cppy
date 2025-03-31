##Ch5.4 map

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in map(fib, [2, 6, 4]):
    print(i)


# L1 = [1, 28, 36]
# L2 = [2, 57, 9]
# for i in map(min, L1, L2):
    # print(i)


# L = []
# for i in map(lambda x, y: x**y, [1 ,2 ,3, 4], [3, 2, 1, 0]):
    # L.append(i)
# print(L)

