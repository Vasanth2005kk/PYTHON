n = int(input("enter the student:"))
student_marks = {}
total=0
for _ in range(n):
    name, *line = input("name and mork:").split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("enter the student name:")
if student_marks.get(query_name):
    for i in student_marks.get(query_name):
        total+=i/len(student_marks.get(query_name))
    print("{0:.2f}".format(total))
