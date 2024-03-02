import datetime

cournt_time=datetime.datetime.now()
birthday=datetime.datetime(2005,3,5)
deffernce=cournt_time-birthday

year=cournt_time.year-birthday.year
print("total year",year)
month=((year-1)*12)+cournt_time.month
print("total month",month)
print("total days:",deffernce.days)
mint=deffernce.total_seconds()
print("total minuts:",mint)