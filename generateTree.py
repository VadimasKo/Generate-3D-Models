import sys
import random

class Point:
    def __init__(self,x,z,y): # Point constructor, y is vertical ax
        self.x = x
        self.z = z
        self.y = y

    def changePosition(self,x,z,y): #changes position of the point
        self.x += x
        self.z += z
        self.y += y

def calculateX(radius): #gives position of point on circle, for hexagon
    x = radius/ 2
    return x

def calculateZ(radius):
    z = radius * 0.866
    return z

class TrunkBisection: #hexagon shaped trunk part
    def __init__(self, radius, height, origin):
        deltaX = calculateX(radius)
        deltaZ = calculateZ(radius)
        self.height = height

        #making vertices of lower hexagon
        self.vertices = [Point(origin.x+radius,origin.z, origin.y)] # angle ->0,360
        self.vertices.append(Point(origin.x+deltaX, origin.z+deltaZ, origin.y)) # angle ->60
        self.vertices.append(Point(origin.x-deltaX, origin.z+deltaZ, origin.y)) # angle ->120
        self.vertices.append(Point(origin.x-radius, origin.z, origin.y)) # angle ->180
        self.vertices.append(Point(origin.x-deltaX, origin.z-deltaZ, origin.y)) # angle ->240
        self.vertices.append(Point(origin.x+deltaX, origin.z-deltaZ, origin.y)) # angle ->300

        #making vertices of upper hexagon
        #for i in range(0,6):
        # self.vertices.append(self.vertices[i].x, self.vertices[i].z, self.vertices)

    def __str__(self): #has __repr__ in it
        output = ""
        for point in self.vertices: # "printing" vertices of lower hexagon
            output += str(point.x) +" "+ str(point.z) +" "+ str(point.y) +"\n"

        for point in self.vertices: # "printing" vertices of upper hexagon  
            output += str(point.x) +" "+ str(point.z) +" "+ str(point.y + self.height) +"\n"
        return output

class Trunk:
    def __init__(self):
        radius = 2              #starting radius
        radiusStep = 0.1        #maximum radius step
        radiusMin = 0.5         #defines stoping point
        minPosChange = -2      
        maxPosChange = 2        #how much can one bisection shift on x/z axys
        minDistanceBetweenBisections = 0.5
        maxDistanceBetweenBisections = 4
        origin = Point(0,0,0)   #starting point, a center of hexagon
        self.bisections = []         #list of trunk bisections

        while radius >= 1:
            height = random.uniform(0.5,3) #generating height of bisection
            self.bisections.append(TrunkBisection(radius,height,origin)) #creating bisection

            deltaX = random.randrange(minPosChange,maxPosChange,1)
            deltaZ = random.randrange(minPosChange,maxPosChange,1)
            deltaY = height + random.uniform(minDistanceBetweenBisections,maxDistanceBetweenBisections)
            origin.changePosition(deltaX,deltaZ,deltaY)   #changing origin point

            radius -= random.uniform(0,radiusStep) #changing radius 

    def drawTree(self):
        output = "OFF \n"
        wallCount = len(self.bisections)*6 +(len(self.bisections)-1)*6
        output += str(len(self.bisections)*12)+" "+str(wallCount)+" 0\n"

        for bisection in self.bisections:
            output += bisection.__str__()

        i = 0
        while i < wallCount:
            if i%6 == 5:
                output +="4 "+ str(i)+" " + str(i+6)+" " + str(i+1)+" " +str(i-5) + " 139 96 22\n"
            else:
                output +="4 "+ str(i) +" "+ str(i+6)+" " + str(i+7)+" " + str(i+1) +" 139 96 22\n"
            i +=1

        return output


a = Trunk()

original_stdout = sys.stdout

with open("result.off","w") as f:
    sys.stdout = f
    print (a.drawTree())
    sys.stdout = original_stdout