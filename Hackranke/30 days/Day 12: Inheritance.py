class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        self.avg = sum(self.scores)/len(self.scores)
        self.grade = ''
        if self.avg <= 100 and self.avg >=90:
            self.grade = 'O'
            return self.grade
        elif self.avg < 90 and self.avg >=80:
            self.grade = 'E'
            return self.grade
        elif self.avg < 80 and self.avg >=70:
            self.grade = 'A'
            return self.grade
        elif self.avg < 70 and self.avg >=55:
            self.grade = 'P'
            return self.grade
        elif self.avg < 55 and self.avg >=40:
            self.grade = 'D'
            return self.grade
        elif self.avg < 40:
            self.grade = 'T'
            return self.grade

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())


'''class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName,lastName,idNum,scores):
         self.firstName=firstName
         self.lastName=lastName
         self.idNum=idNum
         self.scores=scores
    def calculate(self):
        count=0
        len_scoures=len(self.scores)
        for i in self.scores:
            count+=i
        grade=int(count/len_scoures)
        if grade>=90 and grade<=100:
            return "Grade: O"
        elif grade>=80 and grade<90:
            return "Grade: E"
        elif grade>=70 and grade<80:
            return "Grade: A"
        elif grade>=55 and grade<70:
            return "Grade: P"
        elif grade>=40 and grade<55:
            return "Grade: D"
        else:
            return "Grade: T"

line = input().split()
firstName = line[0]
lastName = line[1]
if len(line[2])<=7:
    idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())'''