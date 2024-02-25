def BruteForceStringMatch(P, T) -> int:

    #basic operations is the comparision
    n = len(P)
    m = len(T)

    for i in range(n - m):
        j = 0
        while j < m and T[j] == P[j + i]:
            j += 1
        if j == m:
            return i
    return -1


print(BruteForceStringMatch("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "TUVW"))
