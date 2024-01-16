class Person:
    def __init__(self,yourage):
        if yourage<0:
            yourage=0
            self.age=yourage
            print("Age is not valid, setting age to 0.")
        else:
            self.age=yourage

    def amIOld(self):
        if self.age<13:
            print("You are young.")
        elif self.age>=13 and self.age<18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        self.age+=1


t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")