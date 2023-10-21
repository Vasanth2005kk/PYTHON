'''
create a class called Fruit
create a variable color using __init__method
create a object called apple "pass the color variable as a parameter through object'''

class Fruit:
    def __init__(self,color):
        self.color=color
    def fruit(self):
        print("Apple color:",self.color)
appple=Fruit(color="red")
appple.fruit()

