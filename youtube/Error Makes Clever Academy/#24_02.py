'''
Create a base class called Person with a constructor that takes a name as a parameter.
Create a derived class called Student that inherits from Person and has a constructor that takes a parameter called grade.
Write a method in Student to display the name and grade of student.
use super keyword to achieve this.
'''
class Person():
    def __init__(self,name):
        self.name=name
class student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def display(self):
        print("name:",self.name)
        print("grade:",self.grade)
st1=student("vasanth","male")
st1.display()

