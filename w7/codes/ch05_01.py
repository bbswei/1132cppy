##Ch5.1 Tuples


# t1 = ()
# t2 = (1, 'two', 3)
# print(t1)
# print(t2)


# t1 = (1, 'two', 3)
# t2 = (t1, 3.25)
# print(t2)
# print((t1 + t2))
# print((t1 + t2)[3])
# print((t1 + t2)[2:5])


# def intersect(t1, t2):
    # result = ()
    # for e in t1:
        # if e in t2:
            # result += (e,)
    # return result

# if __name__ == "__main__":
    # print(intersect((1, 'two', 3), (1, 'two', 4)))


# def findExtremeDivisors(n1, n2):
    # minVal, maxVal = None, None
    # for i in range(2, min(n1, n2) + 1):
        # if n1 % i == 0 and n2 % i == 0:
            # if minVal == None:
                # minVal = i
            # maxVal = i
    # return (minVal, maxVal)

# if __name__ == "__main__":
    # minDivisor, maxDivisor = findExtremeDivisors(100, 200)
    # print(minDivisor)
    # print(maxDivisor)
