import string


def getPositionOfLetters(target: str):
    result = string.ascii_letters
    lst = [x for x in result]
    targetLst = [lst.index(x) + 1 for x in target]
    print(targetLst)
    return sum(targetLst)


def tubolationFib(n: int):
    arr = [0, 1]
    for i in range(2, n):
        arr.append(arr[i-2] + arr[i-1])



    print(arr)
    return arr[len(arr)-1]


def changeCoin(target):
    arr = [1,25,10,20]
    sum = 0

    usedCoins = []
    arr.reverse()
    currIdx = 0
    while target > 0:
       diff = target - arr[currIdx]
       print(diff, target, arr[currIdx])
       if 0 < diff < target:
            usedCoins.append(arr[currIdx])
            target += -arr[currIdx]
       else:
            while diff < 0:
                currIdx += 1
                diff = target - arr[currIdx]
                print(diff)
            usedCoins.append(arr[currIdx])
            target += -arr[currIdx]






       currIdx = 0

    print(usedCoins)
    return len(usedCoins)




if __name__ == '__main__':
    # sum = getPositionOfLetters("abcdefghijklmnopqrstuvwxyz")
    # print(sum)
    #
    # anws = tubolationFib(10)
    # print(anws)

    print(changeCoin(100))
