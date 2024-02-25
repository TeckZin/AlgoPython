def question1(input: int):
    n = input
    # n the input size

    summation = 0  # 1

    for i in range(n + 1):  # n + 1
        summation = summation + i  # n -> basic operation

    # (1) +(n+1) + (n) = 2n+2

    #  O(n) remove all coefficients and constants

    print(summation)


def question2(input: int):
    n = input
    # n will be the input size

    summation = 1  # 1

    for i in range(1, n):  # n + 1
        summation = summation * i  # n

    # O(n) remove all coefficients and constants
    print(summation)


def question3_Unsorted(input: list[int]):
    n = len(input)

    largest = 0  # 1

    for i in range(n):  # n + 1
        largest = largest < input[i] if input[i] else largest  # n comparison

    # 1 + n + 1 + n  = 2n+2 will be O(n)
    return largest


def question3_Sorted(input: list[int]):
    # assuming sorted
    n = len(input)
    return input[n - 1]  # just return the largest O(1)


def question3_Indistinct(input: list[int]):
    n = len(input)

    return n == 0 if None else input[0]  # just return any element in the list O(1)


def question4(input1: int, input2: int):
    n = input1 + input2  # the inpute size of n will be the combinaton of bits for both inputs
    c = 0
    while input2 != 0: # the wrost case for thie algorithm will be O(n) being it can only run from input 1 to input 2

        r = input1 % input2
        input1 = input2

        input2 = r

        c += 1


    return input1, c

def runQuesiton4():
    arr = [[20,10], [60,24], [60, 0], [10, 45], [1701, 3768]]

    for i in range(len(arr)):
        ans, c = question4(arr[i][0], arr[i][1])

        print(f"answ: {ans}, c: {c}, diff: {arr[i][0] - arr[i][1]}")



runQuesiton4()

question1(10)

question2(10)
