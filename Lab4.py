import math


# basic operations would be computing the math n ** 2
def closetPair(array: list[tuple]):
    n = len(array)
    # print(array[0][1])
    # print(n)

    d = math.sqrt((((array[0][0] - array[1][0]) ** 2) + ((array[0][1] - array[1][1]) ** 2)))

    for i in range(1, n - 1):
        print("here")
        for j in range(i+1, n):

            d = min(d, math.sqrt((((array[i][0] - array[j][0]) ** 2) + ((array[i][1] - array[j][1]) ** 2))))
            print(d)

    return d


array = [(4, 1), (7, 2), (5, 8)]
print(closetPair(array))
