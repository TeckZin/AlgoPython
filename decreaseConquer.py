import math

"""
using binary search 
O(log n * log m) since n * n so n == m 
thus O(log n * log n) < O(n)  



"""





def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(matrix)

    print("final point: " + str(varSizeDecrease(matrix, 4)))

    print("Starting")


def varSizeDecrease(matrix: list[list[int]], target):
    totalSize = len(matrix) * len(matrix[0])

    l = 0
    r = totalSize
    mid = 0


    """
    binary search decrease by variable of 2  
    
    """
    while l <= r:


        mid = math.floor((l + (r) )/ 2)
        # print((l + r)/2 )
        # print("curr mid: " + str(mid))
        # print("l: " + str(l) + " ,r: " + str(r))

        el = getValue(mid, matrix)
        if el == target:
            return mid

        elif el < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1

"""
return the value using a linear index, by finding the x and y of a matrix 
and returning the value that match 

"""



def getValue(mid, matrix):
    y = mid % len(matrix)
    x = math.floor(mid / len(matrix))
    # print("")
    # print("remainder (y) : " + str(y), "dived (x): " + str(x))
    # print("mid point: " + str(mid))
    # print("point: " + str(matrix[x][y]))

    return matrix[x][y]


if __name__ == '__main__':
    main()
