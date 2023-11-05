'''create a class called Animal with a method sound() that prints "Animal makes a sound."
 cerate a derived class called Dog that inherits form Amimal and overrides the sound() method to print "Dog barks."
 create another derived class called Bird that inherits from animale and overrides the sound() method to print "Birds sing." '''
class Animal():
    def sound(self):
        print("Animal marks a sound.")
class Dog(Animal):
    def sound(self):
        print("Dog barks.")
class Bird(Animal):
    def sound(self):
        #super().sound()
        print("Birds sing")
        super().sound()
Bird_1=Bird()
Bird_1.sound()