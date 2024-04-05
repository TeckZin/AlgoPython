def func(arr: list[int], l: int, u: int) -> list[int]:
    s = [0 for x in range(len(arr))]
    d = [0 for x in range(u - l + 1)]

    for x in arr:
        d[x - l] += 1

    print(s, d)

    for j in range(1, u - l + 1):
        d[j] += d[j - 1]

    print(s, d)

    for i in range(len(arr) - 1, -1, -1):
        j = arr[i] - l
        s[d[j] - 1] = arr[i]
        d[j] += -1

    print(s, d)
    return s


if __name__ == '__main__':
    print("Starting")

    func([13, 11, 12, 13, 12, 12], 11, 13)
