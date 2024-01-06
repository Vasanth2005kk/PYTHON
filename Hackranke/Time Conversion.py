
import datetime 
import re

list_1=[]
list_2=[]

time_check=input()
varible=time_check.split(":")
for i in varible:
    if i.isdigit():
        list_1.append(int(i))
    elif re.findall("PM$",i):
        list_2.append(i.split("PM"))
    else:
        list_2.append(i.split("AM"))
if re.findall("AM$",time_check):
    if list_1[0]==12:
        time=datetime.time(00,list_1[1],int(list_2[0][0]))
        print(time)
    else:
        time=datetime.time(list_1[0],list_1[1],int(list_2[0][0]))
        print(time)
else:
    if list_1[0]==12:
        time=datetime.time(list_1[0],list_1[1],int(list_2[0][0]))
        print(time)
    else:
        time=datetime.time(list_1[0]+12,list_1[1],int(list_2[0][0]))
        print(time)
