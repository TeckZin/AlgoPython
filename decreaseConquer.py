import math


class DFS:
    arr: dict[int: list[int, list[int]]] = {0: []}
    target:int = None

    def __init__(self, arr: dict[int: list[int, list[int]]], target):


        """


        arr: {} list of points and marker

        arr[0] being the node/key

        arr[1] being the marker at [0]/arr[1][0] and a list of node it can traverse to
        being [1] == arr[1][1]
       """
        self.target = target

        self.arr = arr
        self.dfs_main()

    def dfs_main(self):

        count = 0
        # vist of nodes from thekey
        V = self.arr.keys()

        # print(V)

        # print(self.arr[0][0])
        lastVertex: int = None
        for vertex in V:

            print(vertex)

            if vertex == self.target:
                adjacency = self.arr[vertex][1]
                self.arr[lastVertex][1] = adjacency
                self.arr.remove(vertex)


            # loop through all the vertices and checking if it is visited

            if self.arr[vertex][0] == 0:
                # if not visited traverse to that point and check its traversable node
                # using dfs function with the vertex and count
                self.dfs(vertex, count)
            lastVertex = vertex
            # print(vertex)

        # for vertex in V:
        #     print(self.arr[vertex])

    def dfs(self, vertex, count):

        count += 1
        # since it tranver to this node it will be mark
        self.arr[vertex][0] = count

        # all the traversable node/verties
        adjacent = self.arr[vertex][1]
        for w in adjacent:
            # if traversable are not mark recur this function and keep repeating until
            # all traversable of that node and its node are all marked
            if self.arr[w][0] == 0:
                self.dfs(w, count)






def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(matrix)

    print("final point: " + str(varSizeDecrease(matrix, 4)))

    print("Starting")

    graph = [[1,[2, 4]], [2, [5]], [3, [2]], [4, [3]], [5, [6]], [6, [None]]]

    dfs_arr = {0: [0, [1, 2, 3]], 1: [0, [0]], 2: [0, [0, 3, 4]], 3: [0, [0, 2]], 4: [0, [2]]}

    print(DFS(dfs_arr, 1))



"""
using binary search 
O(log n * log m) since n * n so n == m 
thus O(log n * log n) < O(n)  



"""

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
def twoWayBinarySearch(a: list[int], x):

    l = 0
    r = len(a)

    while l <= r:
        mid = math.floor(l + (r - 1)/2)

        if a[mid] == x:
            return mid
        elif a[mid] >= x:
            r = mid - 1
        else:
            l = mid + 1


    return - 1




if __name__ == '__main__':
    main()


