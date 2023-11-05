'''create a class called student
create a variable = name and register number using constructor.
create a function called display which should display the name and register number of the student
'''
class student:
    def __init__(self):
       self.name = "vasanth"
       self.register_number = 21622214112
    def display(self):
        print("Name:",self.name)
        print("Register Number:",self.register_number)
called=student()
called.display()
called1=student()
called1.name="hari"
called1.register_number=2162224578
called1.display()

'''
class student:
    name=""
    register_number=0
    def display(self):
        print("Name:",self.name)
        print("Register Number:",self.register_number)
called=student()
called.name="vasanth"
called.register_number=21322214112
called.display()
'''
