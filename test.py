import math
import numpy as np


def find_triangle(point1, point2, midpoint, targetPoint):
    distancePoint1TargetPoint = distance_calulator(point1, targetPoint)
    distancePoint2TargetPoint = distance_calulator(point2, targetPoint)


    print(distancePoint1TargetPoint, distancePoint2TargetPoint)

    pointToTarget = distancePoint1TargetPoint if distancePoint1TargetPoint < distancePoint2TargetPoint else distancePoint2TargetPoint

    print(pointToTarget)

    midToTarget = distance_calulator(midpoint, targetPoint)
    pointToMid = distance_calulator(point1, midpoint)

    angle = get_angle(pointToMid, pointToTarget, midToTarget)

    return angle


def get_angle(pointToMid, pointToTarget, midToTarget):
    # print(f"getting angle: pointToMid: {pointToMid}, midToTarget: {midToTarget}, pointToTarget: {pointToTarget},")

    dom = (midToTarget ** 2) + (pointToMid ** 2) - (pointToTarget ** 2)

    num = (2 * pointToMid * midToTarget)

    final = dom / num

    print("here: " + str(final))
    return np.arccos(final) * (180 / math.pi)


def distance_calulator(p1, p2):
    return math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))


print(find_triangle((7, 7), (0, 3), (3.5, 5), (0, 6)))
