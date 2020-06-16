import Point
import itertools

class Robot:
    def __init__(self, start = 0, end = 0):
        self.location = start
        self.end = end

    def __str__(self):
        answer = ""
        if(self.location == self.end):
            return ("The starting point and the ending point are the same")
        else:
            return self.findPath(self.location, self.end, answer)

    def north(self, location, end, answer):
        self.location.y += 1
        return self.findPath(self.location, self.end, answer + "N")
    def south(self, location, end, answer):
        self.location.y -= 1
        return self.findPath(self.location, self.end, answer + "S")
    def east(self, location, end, answer):
        self.location.x += 1
        return self.findPath(self.location, self.end, answer + "E")
    def west(self, location, end, answer):
        self.location.x -= 1
        return self.findPath(self.location, self.end, answer + "W")
    
    def solution(self, answer):
        cArray = []
        cArray = answer
        sArray = []
        for i in itertools.permutations(cArray):
            sArray.append(''.join(i))
        sArray = list(dict.fromkeys(sArray))
        print(*sArray, sep = "\n")
        return ("Number of paths: " + str(len(sArray)))

    def findPath(self, location, end, answer):
        #reached the endpoint
        if(location == end):
            finalAnswer = answer + "\n"
            return self.solution(answer)
            
        #South of endpoint
        if(location.y < end.y):          
            return self.north(location, end, answer)
        #North of endpoint
        elif(location.y > end.y): 
            return self.south(location, end, answer)
        #West of endpoint
        elif(location.x < end.x):
            return self.east(location, end, answer)
        #East of endpoint
        elif(location.x > end.x):
            return self.west(location, end, answer)


