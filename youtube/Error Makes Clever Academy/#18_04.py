'''Create a class called calculator
Create 2 variables a and b
Create a function called add,sub,mul,div all functions should take 2 variables as parameter.
Pass the a and b value through object().
'''
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("addition:",self.a+self.b)
    def sub(self):
        print("subtreaction:",self.a-self.b)
    def mul(self):
        print("multiple:",self.a*self.b)
    def div(self):
        print("division:",self.a/self.b)
c=calculator(10,2)
c.add()
c.sub()
c.mul()
c.div()
