'''
create a base class called Employee with properties name and salary.
Create a derived class called Manager that inherits from Employee and adds a property department.
Write a method in Manager to display the name, salary, and department of the manager
'''
class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Manager(Employee):
    def __init__(self,department):
        self.department=department
        super().__init__(name="vasanth", salary=50000)
    def display(self):
        print("name:",self.name)
        print("salary:",self.salary)
        print("department:",self.department)

manager_to_employee=Manager("EEE")
manager_to_employee.display()