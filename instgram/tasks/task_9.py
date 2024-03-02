subject={
    "1":"tamil",
    "2":"math",
    "3":"c++",
    "4":"html",
    "5":"python",
    "6":"english",
    "7":"AI",
    "8":"java",
    "9":"brack",
    "10":"lunch",
    "11":"not is a time in timetable "
}

import datetime

time=list(map(int,input("HH:MM this formet type==>:").split(":")))
value=datetime.time(time[0],time[1])

output=int(value.strftime("%H%M"))

if output>920 and output<=1013:
    print(subject.get("1"))
elif output>1013 and output<=1045:
    print(subject.get("2"))
elif output>1045 and output<=1100:
    print(subject.get("9"))
elif output>1100 and output<=1153:
    print(subject.get("3"))
elif output>1153 and output<=1245:
    print(subject.get("4"))
elif (output>1245 and output<1259) or (output>=100 and output<=130):
    print(subject.get("10"))
elif output>130 and output<=215:
    print(subject.get("5"))
elif output>215 and output<=240:
    print(subject.get("6"))
elif output>240 and output<=254:
    print(subject.get("9"))
elif output>254 and output<=335:
    print(subject.get("7"))
elif output>335 and output<=415:
    print(subject.get("8"))
else:
    print(subject.get("11"))