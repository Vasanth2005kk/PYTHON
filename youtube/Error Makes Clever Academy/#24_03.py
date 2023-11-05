'''Create a base class called Vehicle with a method start() that prints "Vehicle started."
Create a derived class called Car that inherits
from Vehicle and overrides the start() method to print "Car started."
'''
class Vehicle():
    def start(self):
        print("Vehiicle started.")

class car(Vehicle):
    def start(self):
        #super().start()
        print("car started.")
car_start=car()
car_start.start()