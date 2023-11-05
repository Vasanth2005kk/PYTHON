# elif statement
'''
libarary book fees in days for example program
condition:
0 days= no fine
1-5   = 0.5 fine
5-10  = 1 fine
10-30 = 5 fine
above 30 days =membership cancel
'''
days=int(input("enter the days:"))
if days==0:
    print("good no fine")
elif days>=1 and days<=5:
    print("fine amount:",days*0.5)
elif days>5 and days<=10:
    print("fine amount:",days*1)
elif days>10 and 30>=days:
    print("fine amount:",days*5)
else:
    print("menbership cancel")
