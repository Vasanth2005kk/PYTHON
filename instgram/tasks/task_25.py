import calendar

month_year=input("enter the month and year :").split(" ")

print(calendar.month(int(month_year[1]),int(month_year[0])))