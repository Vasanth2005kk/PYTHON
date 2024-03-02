import datetime

time=datetime.datetime.now()
output=int(time.strftime("%H%M"))

if output>=500 and output<1159:
    print("good moring")
elif output>=1200 and output<1659:
    print("good afternoon")
elif output>=1700 and 2159:
    print("good evening")
else:
    print("good night")