import Point
import TheGreedyRobot
import sys

x1 = eval(sys.argv[1])
y1 = eval(sys.argv[2])
x2 = eval(sys.argv[3])
y2 = eval(sys.argv[4])
p1 = Point.Point(x1,y1)
p2 = Point.Point(x2,y2)


print(TheGreedyRobot.Robot(p1,p2))
