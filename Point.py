class Point():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def getX(self):
        return self.x

    def setX(self,newX):
        self.x=newX

    def setY(self,newY):
        self.y=newY

    def getY(self):
        return self.y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __str__(self):
        return "(" + str(self.getX()) + "," + str(self.getY()) + ")"




