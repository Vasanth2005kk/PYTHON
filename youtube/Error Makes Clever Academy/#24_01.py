'''Create a base class called Shape with a method area() that returns 0.
Create a derived class called Rectangle
that inherits from Shape and overrides the area() method to calculate and return the area of a rectangle.
'''
class shape():
    def area(self):
        return 0
class Rectangle(shape):
    def area(self):
        leanth=12
        breath=15
        return leanth*breath
Rectangle_area=Rectangle()
print(Rectangle_area.area())