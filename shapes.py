import matplotlib.pyplot as plt
plt.style.use('bmh')
class Shapes:
    def __init__(self, base,height,color):
        self.base = base
        self.height = height
        self.color = color
        self.perimeter = 
class Rectangle:
    def __init__(self,base,height,color):
        self.base = base
        self.height = height
        self.color = color
        self.perimeter = 2*base + 2*height
        self.area = base*height
        self.vertices = [(0,0),(0,height),(base,height),(base,0),(0,0)]
    def describe(self):
        print("Base: {}".format(self.base))
        print("Height: {}".format(self.height))
        print("Color: {}".format(self.color))
        print("Perimeter: {}".format(self.perimeter))
        print("Area: {}".format(self.area))
        print("Vertices: {}".format(self.vertices))
    def render(self):
        plt.plot(
        [0, 0, self.base, self.base,0],  # X-values
        [0, self.height, self.height, 0,0],   # Y-values
        color='{}'.format(self.color)
        )
        plt.gca().set_aspect("equal")
        plt.savefig('rectangle.png')


class RightTriangle:
    def __init__(self, base, height, color):
        self.base = base
        self.height = height
        self.color = color
        self.perimeter = base + height + (base**2 +height **2)**(1/2)
        self.area = (base * height)/2
        self.vertices = [(0,0),(0,self.height),(self.base,0),(0,0)]
    def describe(self):
        print("Base: {}".format(self.base))
        print("Height: {}".format(self.height))
        print("Color: {}".format(self.color))
        print("Perimeter: {}".format(self.perimeter))
        print("Area: {}".format(self.area))
        print("Vertices: {}".format(self.vertices))
    def render(self):
        plt.plot(
        [0, 0, self.base,0],  # X-values
        [0, self.height, 0,0],   # Y-values
        color='{}'.format(self.color)
        )
        plt.gca().set_aspect("equal")
        plt.savefig('right-triangle.png')
    

class Square(Rectangle):
    def __init__(self,base,color):
        super().__init__(base,height,color)
        =height
        self.perimeter=4*base
        self.area=base**2
        self.vertices=[(0,0),(0,self.base),(self.base,self.base),(self.base,0),(0,0)]
    def describe(self):
        print("Base: {}".format(self.base))
        print("Height: {}".format(self.base))
        print("Color: {}".format(self.color))
        print("Perimeter: {}".format(self.perimeter))
        print("Area: {}".format(self.area))
        print("Vertices: {}".format(self.vertices))
    def render(self):
        plt.plot(
        [0, 0, self.base, self.base,0],  # X-values
        [0, self.base, self.base, 0,0],   # Y-values
        color='{}'.format(self.color)
        )
        plt.gca().set_aspect("equal")
        plt.savefig('Square.png')


rect = Rectangle(5,2,'red')
rect.describe()
rect.render()

plt.clf()

tri = RightTriangle(5,2,'blue')
tri.describe()
tri.render()

plt.clf()

sq = Square(5,'green')
sq.describe()
sq.render()