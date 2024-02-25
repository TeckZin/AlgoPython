import math
import numpy as np


class convex_hull_problem:
    arrPoints: list[tuple[int, int]] = []
    convexPoint: list[tuple[int, int]] = []
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

        print(self.highestX)
        print(self.highestY)
        print(self.lowestX)
        print(self.lowestY)
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
        self.convex_hull_main()

        print("result: " + str(self.convexPoint))

    def convex_hull_main(self):

        self.arrPoints = self.sort_array(self.arrPoints)
        print("convexPoints: " + str(self.convexPoint))

        self.convexPoint = self.sort_array(self.convexPoint)

        print("convex: " + str(self.convexPoint))

        for point in self.arrPoints:
            print("-" * 20)
            print("new point:" + str(point))

            top = False
            bottom = False
            left = False
            right = False

            if point not in self.convexPoint:
                print(self.convexPoint)
                self.convexPoint.append(point)
                print(self.convexPoint)
                self.convexPoint = self.sort_array(self.convexPoint)
                print(self.convexPoint)
                index = self.convexPoint.index(point)
                print(index)
                flag = True
                firstPoint = ()
                secondPoint = ()
                if index + 1 != len(self.convexPoint):
                    firstPoint = self.convexPoint[index - 1]
                    secondPoint = self.convexPoint[index + 1]
                elif index + 1 == len(self.convexPoint):
                    firstPoint = self.convexPoint[index - 1]
                    secondPoint = self.convexPoint[0]

                print(firstPoint, secondPoint)
                self.convexPoint = self.sort_array(self.convexPoint)
                print(self.convexPoint)
# top right

                # bottom left
                if firstPoint[0] <= secondPoint[0] and firstPoint[1] <= secondPoint[1]:
                    # top right

                    print("top right")
                    if firstPoint[1] <= point[1] and secondPoint[0] >= point[0]:
                        flag = False
                elif firstPoint[0] <= secondPoint[0] and firstPoint[1] >= secondPoint[1]:
                    # bottom right
                    print("bottom right")
                    if point[0] >= firstPoint[0] and point[1] >= secondPoint[1]:
                        flag = False

                # check the directorion

                if flag: self.convexPoint.remove(point)

                print("stage fine: " + str(self.convexPoint))
        return

    def find_triangle(self, point1, point2, midpoint, targetPoint):
        distancePoint1TargetPoint = self.distance_calulator(point1, targetPoint)
        distancePoint2TargetPoint = self.distance_calulator(point2, targetPoint)
        pointToTarget = distancePoint1TargetPoint if distancePoint1TargetPoint < distancePoint2TargetPoint else distancePoint2TargetPoint

        midToTarget = self.distance_calulator(midpoint, targetPoint)
        pointToMid = self.distance_calulator(point1, midpoint)

        angle = self.get_angle(pointToMid, pointToTarget, midToTarget)

        return angle

    def get_angle(self, pointToMid, pointToTarget, midToTarget):

        # print(f"getting angle: pointToMid: {pointToMid}, midToTarget: {midToTarget}, pointToTarget: {pointToTarget},")

        dom = (midToTarget ** 2) + (pointToMid ** 2) - (pointToTarget ** 2)

        num = (2 * pointToMid * midToTarget)

        num = dom / num
        return np.arccos(num) * (180 / math.pi)

    def distance_calulator(self, p1, p2):
        return math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))

    def mid_point_function(self, point1: tuple[int, int], point2: tuple[int, int]) -> tuple[float, float]:

        x: float = (point1[0] + point2[0]) / 2
        y: float = (point1[1] + point2[1]) / 2
        return x, y

    def sort_array(self, arr):

        # print("before sorted: " + str(self.convexPoint))

        # distance = math.sqrt(((point1[0] - point2[0]) ** 2) + ((point2[1] - point2[1]) ** 2))

        currPoint = self.lowestX
        tempConvexPoints = arr
        tempConvexPoints.remove(currPoint)
        otherConvexPoints = [currPoint]
        for i in range(len(arr)):
            index = 0

            tempPoint = [0, (0, 0)]

            for point2 in tempConvexPoints:
                # distanceX is the differnece between piont2 and selected point
                distanceX = abs(point2[0] - currPoint[0])
                # print("currPoint: " + str(currPoint) + " otherPoint: " + str(point2) + " tempPoint: " + str(tempPoint) + " distanceX: " + str(distanceX) + " index: " + str(index))
                if index != 0:
                    if distanceX == 0 and point2[1] > currPoint[1]:
                        # print("second here")
                        tempPoint = [distanceX, point2]
                    elif distanceX <= tempPoint[0] and tempPoint[1][1] < point2[1]:
                        # print("here")
                        tempPoint = [distanceX, point2]


                else:
                    tempPoint = [distanceX, point2]

                index += 1
            otherConvexPoints.append(tempPoint[1])
            tempConvexPoints.remove(tempPoint[1])
            currPoint = tempPoint[1]
        # print("sorted:" + str(otherConvexPoints))
        return otherConvexPoints


def dfs():
    return


def bfs(arr: list[tuple[int, int]]):
    for x in arr:
        print(x)
    return


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
