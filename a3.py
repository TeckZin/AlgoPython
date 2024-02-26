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
        if len(self.convexPoint) == 0:

            if self.highestX not in self.convexPoint:
                self.convexPoint.append(self.highestX)
            if self.lowestX not in self.convexPoint:
                self.convexPoint.append(self.lowestX)
            if self.highestY not in self.convexPoint:
                self.convexPoint.append(self.highestY)
            if self.lowestY not in self.convexPoint:
                self.convexPoint.append(self.lowestY)

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

    def convex_hull_main(self):
        currPoint = self.lowestX

        self.finalConvexPoint.append(currPoint)

        topRight = True
        bottomRight = False
        bottomLeft = False
        topLeft = False
        for i in range(len(self.arrPoints)):

            """
            debugging logs  
            """
            # print("--" * 100)

            potentialPoint = []

            """
            debugging logs  
            """
            # print("currPoint: " + str(currPoint))
            # print("convexPoints: " + str(self.finalConvexPoint))
            # print("currPoint: " + str(currPoint))
            if currPoint != self.highestY or topRight:
                """
                debugging logs  
                """
                # print("topRight")
                for point in self.arrPoints:
                    if point[1] >= currPoint[1]:

                        """
                        debugging logs  
                        """
                        # print("point: " + str(point))
                        if point not in self.finalConvexPoint:
                            potentialPoint.append(point)
                            topRight = True

            if currPoint == self.highestY or bottomRight:
                """
                debugging logs  
                """
                # print("bottomRight")
                topRight = False

                for point in self.arrPoints:

                    if point[0] >= currPoint[0] and point not in self.finalConvexPoint:
                        potentialPoint.append(point)
                        bottomRight = True

            if currPoint == self.highestX or bottomLeft:
                bottomRight = False
                """
                debugging logs  
                """
                # print("bottomLeft")
                potentialPoint = []
                topRight = False
                for point in self.arrPoints:
                    if point[1] <= currPoint[1] and point not in self.finalConvexPoint:
                        potentialPoint.append(point)
                        bottomLeft = True

            if currPoint == self.lowestY or topLeft:

                potentialPoint = []
                bottomLeft = False
                """
                debugging logs  
                """
                # print("topLeft")
                # print("currPoint: " + str(currPoint))
                for point in self.arrPoints:
                    if point[0] <= currPoint[0]:
                        print(point)
                        potentialPoint.append(point)
                        topLeft = True
            if currPoint == self.lowestX and len(potentialPoint) == 0:
                return

            """
            debugging logs  
            """
            # print("potential points: " + str(potentialPoint))
            if topLeft:

                """
                debugging logs  
                """
                # print("topLeft loop")
                closetYPoint = [0.0, (0.0, 0.0)]
                index = 0
                diffY0 = False
                diffY0Points = [0.0, (0.0, 0.0)]
                for point in potentialPoint:
                    """
                    debugging logs  
                    """
                    # print("point: " + str(point))
                    diffY = float(abs(currPoint[1] - point[1]))

                    if index == 0:
                        closetYPoint = [diffY, point]
                    elif diffY == 0:
                        diffY0 = True
                        diffY0Points.append(point)
                    elif closetYPoint[0] > diffY:
                        closetYPoint = [diffY, point]
                    elif closetYPoint[0] == diffY:
                        diffX1 = abs(closetYPoint[1][0] - currPoint[0])
                        diffX2 = abs(point[0] - currPoint[0])

                        closetYPoint = [diffY, point] if diffX1 < diffX2 else closetYPoint
                    """
                    debugging logs  
                    """
                    # print("closetYPoint: " + str(closetYPoint))
                    index += 1

                j = 0

                if diffY0:
                    for point in diffY0Points:
                        diffX = abs(currPoint[0] - currPoint[1])
                        if j == 0:
                            closetYPoint = [diffX, point]
                        elif closetYPoint[0] > diffX:
                            closetYPoint = [diffX, point]

                    j += 1

                currPoint = closetYPoint[1]

                if currPoint not in self.convexPoint:
                    self.convexPoint.append(currPoint)
                    self.finalConvexPoint.append(currPoint)
                elif currPoint in self.finalConvexPoint and currPoint == self.lowestX:
                    """
                    debugging logs  
                    """
                    # print("DONE DONE")
                    # print(self.finalConvexPoint)
                    return self.finalConvexPoint
                self.arrPoints.remove(currPoint)


            elif bottomLeft:

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
                # print("cloestXpoint: " + str(closetXPoint))
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
                    # print("APPPEND CON: " + str(currPoint))

                    self.convexPoint.append(currPoint)
                    self.finalConvexPoint.append(currPoint)

                self.arrPoints.remove(currPoint)




            elif bottomRight:
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


            elif topRight:
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

        return self.finalConvexPoint


class DFS:
    arr: dict[int: list[int, list[int]]] = {0: []}

    def __init__(self, arr: dict[int: list[int, list[int]]]):
        self.arr = arr
        self.dfs_main()

    def dfs_main(self):

        count = 0

        V = self.arr.keys()
        print(V)

        # print(self.arr[0][0])
        for vertex in V:
            if self.arr[vertex][0] == 0:
                self.dfs(vertex, count)
            # print(vertex)

        for vertex in V:
            print(self.arr[vertex])

    def dfs(self, vertex, count):
        count += 1
        self.arr[vertex][0] = count

        adjacent = self.arr[vertex][1]
        for w in adjacent:
            if self.arr[w][0] == 0:
                self.dfs(w, count)


class BFS:
    arr: dict[int: list[int, list[int]]] = {0: []}

    def __init__(self, arr: dict[int: list[int, list[int]]]):
        self.arr = arr
        count = 0
        V = self.arr.keys()
        for v in V:
            if self.arr[v][0] == 0:
                self.bfs(v, count)

        for v in V:
            print(self.arr[v])

    def bfs(self, v, count):
        count += 1
        queue = []
        self.arr[v][0] = count
        while len(queue) != 0:
            for w in self.arr[v][1]:
                if self.arr[w][0] == 0:
                    count += 1
                    self.arr[w][0] = count
                    queue.append(w)
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

# convex_hull_problem(conex_arr)

dfs_arr = {0: [0, [1, 2, 3]], 1: [0, [0]], 2: [0, [0, 3, 4]], 3: [0, [0, 2]], 4: [0, [2]]}

bfs_arr = {0: [0, [1, 2, 3]], 1: [0, [0]], 2: [0, [0, 3, 4]], 3: [0, [0, 2]], 4: [0, [2]]}
# DFS(dfs_arr)

BFS(bfs_arr)
