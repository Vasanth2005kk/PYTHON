import datetime as cal
month,day,year=input("enter the month day and year with in spece type:").split()
current =cal.date(int(year),int(month),int(day))
s = current.strftime("%A")
print(s.upper())
