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

        self.convexPoint.sort()
        self.convex_hull_main()

        print(self.convexPoint)

    def convex_hull_main(self):
        for point in self.convexPoint:
            x = point[0]
            y = point[1]

            if point not in self.convexPoint:

                self.convexPoint.append(point)
                self.convexPoint.sort()

                index = self.convexPoint.index(point)

                self.convexPoint.pop(index)

                if index - 1 == len(self.arrPoints) or index == 0:
                    self.convexPoint.append(point)
                else:
                    firstPoint = self.convexPoint[index - 1]
                    secondPoint = self.convexPoint[index + 1]

                    midPoint = self.mid_point_function(firstPoint, secondPoint)

                    if (midPoint[0] > x and midPoint[1] > y) or (midPoint[0] == x and midPoint[1] == y):
                        self.convexPoint.append(point)

        return

    def mid_point_function(self, point1: tuple[int, int], point2: tuple[int, int]) -> tuple[float, float]:
        x: float = (point1[0] - point2[0]) / 2
        y: float = (point1[1] - point2[1]) / 2
        return x, y


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

conex_arr = [(0, 0), (0, 4), (-4, 0), (5, 0), (0, -6), (1, 0)]

convex_hull_problem(conex_arr)
