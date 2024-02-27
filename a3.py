import math
import numpy as np

"""
the class will take in a list of points 
and traverse the points clockwise using the most test point 

to achive this the class/algorithm will use the brute force method 
and check each other with ever other possible points, while implementing some minor optimizations


Time Complexity: O()
Space Complexity: O()

@author: Teck
@params: arr -> list of 2d points 

"""


class convex_hull_problem:
    arrPoints: list[tuple[int, int]] = []
    convexPoint: list[tuple[int, int]] = []
    finalConvexPoint: list[tuple[int, int]] = []
    lowestX: tuple[int, int] = []
    highestX: tuple[int, int] = []
    lowestY: tuple[int, int] = []
    highestY: tuple[int, int] = []

    def __init__(self, arr: list[tuple[int, int]]):
        self.arrPoints = arr

        self.arrPoints.sort()
        index = 0

        """
        getting all four (x, y) coordinates of a group of point, 
        getting the most left (lowest x coord) getting most right (highest x coord)
        getting the top point (highest y coord) getting the lowest (lowest y coord)
        this will set the limit when traversing the coords 
         
        """
        for point in self.arrPoints:
            cX = point[0]
            cY = point[1]
            print("Point: " + str(point))

            if index == 0:
                self.highestX = point
                self.lowestX = point
                self.lowestY = point
                self.highestY = point

            if cX >= self.highestX[0]:
                self.highestX = point
            elif cX < self.lowestX[0]:
                self.lowestX = point

            if cY >= self.highestY[1]:
                self.highestY = point
            elif cY < self.lowestY[1]:
                self.lowestY = point
            index += 1

        """
        debugging logs  
        """
        #
        # print(self.highestX)
        # print(self.highestY)
        # print(self.lowestX)
        # print(self.lowestY)

        # adding the point to potentially convex point array
        if len(self.convexPoint) == 0:

            if self.highestX not in self.convexPoint:
                self.convexPoint.append(self.highestX)
            if self.lowestX not in self.convexPoint:
                self.convexPoint.append(self.lowestX)
            if self.highestY not in self.convexPoint:
                self.convexPoint.append(self.highestY)
            if self.lowestY not in self.convexPoint:
                self.convexPoint.append(self.lowestY)

        # making sure its not repeat due to a triangle is also a polygon and wil also be a hux

        for point in self.arrPoints:
            if (point[0] == self.lowestX or point[0] == self.highestX) and (point not in self.convexPoint):
                self.convexPoint.append(point)
            if (point[1] == self.lowestY or point[1] == self.highestY) and (point not in self.convexPoint):
                self.convexPoint.append(point)
        self.convexPoint.sort()
        answer = self.convex_hull_main()

        """
        debugging logs  
        """
        # print("result: " + str(answer))

    """
    this function is main file to traverse the list of coords
    since the list must be clockwise we will start at the most left move to highest Y
    then most right point most bottom point and finally back to most left 
    
    
    to prevent un convex hull, where it might break towards the center and it should only be 
    traversing outside and do not concave
    
    for each type of traverse ( left -> top, top -> right, right -> bottom, bottom -> left) 
    it will ignore a majority part of the coords, and append those point that could be the next point to traverse
    
    to check out of the potential which is traverse to we will check the x first or y first then x or y visa versa
    depending on type of traverse 
    
    
    it will change the type of traverse when arriving at one of the majoring breaking poit (highest X, highest Y, etc ...)
    
    this take a brute force method of apporach by chekcing each coords with other coords
    
    
    
    """

    def convex_hull_main(self):
        currPoint = self.lowestX

        self.finalConvexPoint.append(currPoint)

        leftTop1 = True
        topRight = False
        rightBottom = False
        bottomLeft = False
        for i in range(len(self.arrPoints)):

            """
            debugging logs  
            """
            # print("--" * 100)

            # points which could be the next traversing point and need more calculations to be decided
            # will be appended here, this DOES NOT MEAN and it will be part of the finalConvexPoint
            potentialPoint = []

            """
            debugging logs  
            """
            # print("currPoint: " + str(currPoint))
            # print("convexPoints: " + str(self.finalConvexPoint))
            # print("currPoint: " + str(currPoint))

            """
            stating at getting left -> top
            potentialPoints  
            
            """
            if currPoint != self.highestY or leftTop1:
                """
                debugging logs  
                """
                # print("topRight")

                # since it is tranversing to the top, any point bellow this curr point will be not considered an
                # a possible point for convex hull. (will be different for hull which is allow to concave"
                for point in self.arrPoints:
                    if point[1] >= currPoint[1]:

                        """
                        debugging logs  
                        """
                        # print("point: " + str(point))
                        if point not in self.finalConvexPoint:
                            potentialPoint.append(point)
                            leftTop1 = True

            """
            after the left -> top is done now its top -> right 
            
            """
            if currPoint == self.highestY or topRight:
                """
                debugging logs  
                """
                # print("bottomRight")
                leftTop1 = False
                # make sure the potentialPoint is empty and doesn't include the content before
                # since it could be potential points before but not for this

                potentialPoint = []

                for point in self.arrPoints:

                    """
                    if the x coords is largest than the highestY coord of X
                    those are the potential points 
                    """

                    if point[0] >= currPoint[0] and point not in self.finalConvexPoint:
                        potentialPoint.append(point)
                        topRight = True

            """
            after the top -> right  is done now its right -> bottom
            
            
            """

            if currPoint == self.highestX or rightBottom:
                topRight = False
                """
                debugging logs  
                """
                # print("bottomLeft")
                potentialPoint = []
                leftTop1 = False
                for point in self.arrPoints:
                    """
                    from the highest x to the lowest y 
                    so anything bellow x will be potential point and get appended 

                    """
                    if point[1] <= currPoint[1] and point not in self.finalConvexPoint:
                        potentialPoint.append(point)
                        rightBottom = True

            """
            after the bottom -> left its is now done and traverse back to the highest x coord
            
            
            """

            if currPoint == self.lowestY or bottomLeft:

                potentialPoint = []
                rightBottom = False
                """
                debugging logs  
                """
                # print("topLeft")
                # print("currPoint: " + str(currPoint))
                for point in self.arrPoints:
                    """
                    lowest Y will try to round back to the lowest X, and append anything that x is lower than it 

                    """
                    if point[0] <= currPoint[0]:
                        print(point)
                        potentialPoint.append(point)
                        bottomLeft = True
            if currPoint == self.lowestX and len(potentialPoint) == 0:
                return

            """
            debugging logs  
            """
            # print("potential points: " + str(potentialPoint))

            """
            from bottom to the left rounding back  
            """
            if bottomLeft:

                """
                debugging logs  
                """
                # print("topLeft loop")

                """
                
                cloestYpoint, being the cloest point to the currNode
                first index is the distance 
                second index is the coord of the point to be use later 
                 
                """
                closetYPoint = [0.0, (0.0, 0.0)]
                index = 0

                """
                diffY0 is there any point ont he same y axies, that means the x won't matter  
                if true will use diff0YPoints instead of cloestX 
                """
                diffY0 = False
                diffY0Points = [0.0, (0.0, 0.0)]
                for point in potentialPoint:
                    """
                    debugging logs  
                    """
                    # print("point: " + str(point))
                    diffY = float(abs(currPoint[1] - point[1]))

                    if index == 0:
                        # first index will be the first point and the list will be empty so add something
                        closetYPoint = [diffY, point]
                    # if true than on the same y axies and need to consider this first not the x
                    elif diffY == 0:
                        diffY0 = True
                        diffY0Points.append(point)
                        # check if which is close to currNode
                    elif closetYPoint[0] > diffY:
                        closetYPoint = [diffY, point]
                    elif closetYPoint[0] == diffY:

                        # check if the cloestYpoint is closer or the new point is closer and tunery it
                        diffX1 = abs(closetYPoint[1][0] - currPoint[0])
                        diffX2 = abs(point[0] - currPoint[0])

                        closetYPoint = [diffY, point] if diffX1 < diffX2 else closetYPoint
                    """
                    debugging logs  
                    """
                    # print("closetYPoint: " + str(closetYPoint))
                    index += 1

                j = 0

                # consider the if on the same y axies
                # if true it will append that coord instead
                if diffY0:
                    for point in diffY0Points:
                        diffX = abs(currPoint[0] - currPoint[1])
                        if j == 0:
                            closetYPoint = [diffX, point]
                        elif closetYPoint[0] > diffX:
                            closetYPoint = [diffX, point]

                    j += 1

                # adding the final point
                # since added this will be the new currPoint and re-run the loop agian
                currPoint = closetYPoint[1]

                if currPoint not in self.convexPoint:
                    self.convexPoint.append(currPoint)
                    # appeding it and it will be in order
                    self.finalConvexPoint.append(currPoint)
                elif currPoint in self.finalConvexPoint and currPoint == self.lowestX:
                    """
                    debugging logs  
                    """
                    # print("DONE DONE")
                    # print(self.finalConvexPoint)
                    return self.finalConvexPoint
                self.arrPoints.remove(currPoint)

                """
                same as the above if statement, just swap the y and x 
                and change the comparison since its going right -> bottom and check for x 
                and compare x  
                
                """
            elif rightBottom:

                """
                debugging logs  
                """
                # print("bottomLeft loop")
                closetXPoint = [0, (0, 0)]
                index = 0
                diffX0 = False
                diffX0Points = [(0, 0)]
                for point in potentialPoint:
                    diffX = abs(currPoint[0] - point[0])
                    if index == 0:
                        closetXPoint = [diffX, point]
                    elif diffX == 0:
                        diffX0 = True
                        diffX0Points.append(point)
                    elif closetXPoint[0] > diffX:
                        closetXPoint = [diffX, point]
                    elif closetXPoint[0] == diffX:
                        diffY1 = abs(closetXPoint[1][0] - currPoint[0])
                        diffY2 = abs(point[0] - currPoint[0])

                        closetXPoint = [diffX, point] if diffY1 < diffY2 else closetXPoint
                    index += 1

                j = 0

                """
                debugging logs  
                """
                # print("closestXpoint: " + str(closetXPoint))
                if diffX0:
                    for point in diffX0Points:
                        # print(diffX0Points)
                        # print(currPoint[1])
                        # print(point[1])
                        diffY = abs(currPoint[1] - point[1])

                        if j == 0:
                            closetXPoint = [diffY, point]
                        elif closetXPoint[0] > diffY:
                            closetXPoint = [diffY, point]

                    j += 1

                currPoint = closetXPoint[1]

                if currPoint not in self.finalConvexPoint:
                    """
                    debugging logs  
                    """
                    # print("APPEND CON: " + str(currPoint))

                    self.convexPoint.append(currPoint)
                    self.finalConvexPoint.append(currPoint)

                self.arrPoints.remove(currPoint)

                """
                same as the above but swap x and y again 
                and check if which is closer to its x,
                check if on the same y axis 
                
                """


            elif topRight:
                """
                debugging logs  
                """

                # print("bottomRightLoop")

                closetYPoint = [0.0, (0, 0)]
                index = 0
                diffY0 = False
                diffY0Points = [0, (0, 0)]
                for point in potentialPoint:
                    """
                    debugging logs  
                    """
                    # print("point: " + str(point))

                    diffY = abs(currPoint[1] - point[1])
                    if index == 0:
                        closetYPoint = [diffY, point]
                    elif diffY == 0 and point[1] > closetYPoint[1][1]:
                        diffY0 = True
                        diffY0Points.append(point)
                    elif diffY < closetYPoint[0]:
                        """
                        debugging logs  
                        """
                        # print("here: " + str(point))
                        closetYPoint = [diffY, point]
                    elif closetYPoint[0] == diffY:
                        diffX1 = abs(closetYPoint[1][0] - currPoint[0])
                        diffX2 = abs(point[0] - currPoint[0])

                        closetYPoint = [diffY, point] if diffX2 < diffX1 else closetYPoint

                    index += 1

                """
                debugging logs  
                """
                # print(closetYPoint)
                if diffY0:
                    j = 0

                    for point in diffY0Points:
                        diffX = abs(point[0] - currPoint[0])
                        if j == 0:
                            closetYPoint = [diffX, point]
                        elif closetYPoint[0] > diffX:
                            closetYPoint = [diffX, point]

                        j += 1

                currPoint = closetYPoint[1]

                if currPoint not in self.finalConvexPoint:
                    """
                    debugging logs  
                    """
                    # print("append point: " + str(currPoint))
                    self.convexPoint.append(currPoint)
                    self.finalConvexPoint.append(currPoint)

                self.arrPoints.remove(currPoint)
                """
                the final loop back 
                switch the x and y from the last elif statement 
                but this time if meet the lowestX it will break and return
                since theory it would have fully loop back  
                
                """

            elif leftTop1:
                """
                debugging logs  
                """
                # print("topRight loop")

                # check for closest x

                closetXPoint = [0, (0, 0)]
                diffX0 = False
                diffX0Points = [(0, 0)]
                index = 0

                for point in potentialPoint:
                    diffX = abs(currPoint[0] - point[0])

                    if index == 0:
                        closetXPoint = [diffX, point]

                    elif diffX == 0:
                        diffX0 = True
                        diffX0Points.append(point)
                    elif diffX < closetXPoint[0]:
                        closetXPoint = [diffX, point]


                    elif closetXPoint[0] == diffX:
                        diffY1 = abs(closetXPoint[1][0] - currPoint[0])
                        diffY2 = abs(point[0] - currPoint[0])

                        closetXPoint = [diffX, point] if diffY2 < diffY1 else closetXPoint
                    index += 1
                if diffX0:
                    j = 0
                    for point in diffX0Points:
                        diffY = abs(currPoint[1] - point[1])
                        if j == 0:
                            closetXPoint = [diffY, point]
                        elif closetXPoint[1] > diffY:
                            closetXPoint = [diffY, point]
                        j += 1

                currPoint = closetXPoint[1]

                if currPoint not in self.finalConvexPoint:
                    self.convexPoint.append(currPoint)
                    self.finalConvexPoint.append(currPoint)
                    """
                    debugging logs  
                    """
                    # print("ADDED CURR POINT:  " + str(currPoint))

                self.arrPoints.remove(currPoint)

        """
        debugging logs  
        """
        # print(self.finalConvexPoint)

        # return eh final convex due to have finished looping

        return self.finalConvexPoint


""" 
dfs: depth first search,
using recursion to traverse to the depest part of graph 
backtrack when reach a deep end keep repeat 


could use a stack to for first in last out and added in the node need to be visit 
this will ensure that the depest get first pick 

or use recusion with a marker if not it will tranverse it and fidning the deptest part 

take a dived and conquer approach

"""


class DFS:
    arr: dict[int: list[int, list[int]]] = {0: []}

    def __init__(self, arr: dict[int: list[int, list[int]]]):

        """


        arr: {} list of points and marker

        arr[0] being the node/key

        arr[1] being the marker at [0]/arr[1][0] and a list of node it can traverse to
        being [1] == arr[1][1]
       """

        self.arr = arr
        self.dfs_main()

    def dfs_main(self):

        count = 0
        # vist of nodes from thekey
        V = self.arr.keys()

        # print(V)

        # print(self.arr[0][0])
        for vertex in V:

            # loop through all the vertices and checking if it is visited

            if self.arr[vertex][0] == 0:
                # if not visited traverse to that point and check its traversable node
                # using dfs function with the vertex and count
                self.dfs(vertex, count)
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


"""
almost similar to recur but use while loop instead 


same input of as the dfs function

using a divied and conquer method as well 

instead of visitng the deptest graph it will visited the the cloest depth 
so it will visited all the  nodes at its level before tranversreing to the next
that is why a queue is use and not a stack since the cloest node will be the first appended

"""


class BFS:
    arr: dict[int: list[int, list[int]]] = {0: []}

    def __init__(self, arr: dict[int: list[int, list[int]]]):
        self.arr = arr
        count = 0

        #get the verites of list
        V = self.arr.keys()
        for v in V:

        # check if the all the vertices is marked if not run bfs
            if self.arr[v][0] == 0:
                self.bfs(v, count)

        for v in V:
            print(self.arr[v])

    """
    bfs will call in self if any of the vertices and its tranversable are not marked 
    


    """
    def bfs(self, v, count):
        count += 1
         # first in first out
        queue = []
        self.arr[v][0] = count


        """
        
        a queue of node/vertices that need to be visited and will be added to the que
        queue being len of 0 means that all the traversable vertices have been visited for this vertex
        """
        while len(queue) != 0:
            for w in self.arr[v][1]:
                if self.arr[w][0] == 0:
                    count += 1
                    # mark the vertices that have visited
                    self.arr[w][0] = count


                    queue.append(w)
            # after visited it will be pop since it past the if statement
            queue.pop()


# bfsArr = [(1, 2), (2, 3), (3, 4), (4, 3)]
#
# bfs(bfsArr)
#
# testArr = [(1, 2), (1, 1), (3, 1), (3, 2), (2, 4), (2, 1)]
# print(testArr)
#
# testArr.sort()
#
# print(testArr)

conex_arr = [(7, 7),
             (7, 2),
             (0, 6),
             (2, 1),
             (8, 2),
             (6, 4),
             (8, 0),
             (0, 3),
             (8, 3),
             (6, 7),
             (1, 3)]

convex_hull_problem(conex_arr)

dfs_arr = {0: [0, [1, 2, 3]], 1: [0, [0]], 2: [0, [0, 3, 4]], 3: [0, [0, 2]], 4: [0, [2]]}

bfs_arr = {0: [0, [1, 2, 3]], 1: [0, [0]], 2: [0, [0, 3, 4]], 3: [0, [0, 2]], 4: [0, [2]]}

DFS(dfs_arr)

BFS(bfs_arr)
