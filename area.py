class Area:
    result = 0
    def calculatearea(self):
        print("\n\tCalculating area of Rectangle,Circle,Triangle .........")

class Rectangle(Area):
    def calculatearea(self):
        l = int(input("Enter length: "))
        w = int(input("Enter width: "))
        result = l*w
        print("Area of rectangle : ", result)

class Circle(Area):
    def calculatearea(self):
        r = float(input("Enter radius  of circle : "))
        result = 3.14*r*r  
        print("Area of circle : ", result)

s = Area()
s.calculatearea()
r = Rectangle()
r.calculatearea()
c = Circle()
c.calculatearea()
