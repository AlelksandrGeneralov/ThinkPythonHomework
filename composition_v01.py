import math

def area(radius):
    temp = math.pi*radius**2
    return temp

def distance(x1, y1, x2, y2):
    return(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xc, yp)
    result = area(radius)
    print(result)

circle_area(1, 1, 4, 5)