'''
Create a class called teacher
Create a variable = name and register number using constructor
Create a function called display which should display the name and
register number of the teacher
Create t1 and t2 object and pass the name and reg_no value through object
'''
class teacher:
    def __init__(self,name,reg_no):
        self.name=name
        self.reg_no=reg_no
    def sudent(self):
        print("name:",self.name)
        print("regester_number:",self.reg_no)
t1=teacher("vasanth",21622214112)
t2=teacher("ranjith",21622214093)
t1.sudent()
t2.sudent()
